import bs4, requests, webbrowser

# Open "http://www.bom.gov.au/nsw/forecasts/richmond.shtml"
resp = requests.get('http://www.bom.gov.au/nsw/forecasts/richmond.shtml')
resp.raise_for_status()
forecast = bs4.BeautifulSoup(resp.text, 'html.parser')
# Get rain chance from "div.day:nth-child(3) > div:nth-child(2) > dl:nth-child(1) > dd.rain"
rain_element = forecast.select('div.day:nth-child(3) > div:nth-child(2) > dl:nth-child(1) > dd.rain')

# Get the daily summary from "div.day:nth-child(3) > div:nth-child(2) > p:nth-child(3)"
for_sum = forecast.select('div.day:nth-child(3) > div:nth-child(2) > p:nth-child(3)')
for_sum = for_sum[0].getText()

# Extract the chance of rain from the element, strip the white space & then change the string to an integer
rain_chance = rain_element[0].getText()
rain_chance = rain_chance.strip()
rain_chance = rain_chance[-2:]
rain_int = rain_chance.replace('%', '')

# If chance of rain greater than %80 suggest to take the car today
if int(rain_int) > 80:
    print(r'''        ------               _____
       /      \ ___\     ___/    ___
    --/-  ___  /    \/  /  /    /   \
   /     /           \__     //_     \
  /                     \   / ___     |
  |           ___       \/+--/        /
   \__           \       \           /
      \__                 |          /     There are holes in the sky,
     \     /____      /  /       |   /     Where the rain gets in,
      _____/         ___       \/  /\      The holes are very small,
           \__      /      /    |    |     That's why rain is thin.
         /    \____/   \       /   //
     // / / // / /\    /-_-/\//-__-            - Spike Milligan
      /  /  // /   \__// / / /  //
     //   / /   //   /  // / // /
      /// // / /   /  //  / //
   //   //       //  /  // / /
     / / / / /     /  /    /
  ///  / / /  //  // /  // //
     ///    /    /    / / / /
///  /    // / /  // / / /  /
   // ///   /      /// / /
''' + "\n\n The chance of rain is %s today, I'd suggest taking the car instead." % rain_chance + ''''\n\n The forecast is: %s \n\n''' % for_sum )
# If chance of rain < 80% but > 40% then suggest to look into it more
elif 40 < int(rain_int) < 80:
    print('''                _
              (`  ).                   _
             (     ).              .:(`  )`.
)           _(       '`.          :(   .    )
        .=(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .+(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.-(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.''' + "\n\n The chance of rain is %s today, I'd suggest looking at the weather more." % rain_chance + '''\n\n The forecast is: %s \n\n''' % for_sum)
    bom = input("Shall I open the website for you?")
    if bom[0] == 'y':
        webbrowser.open('http://www.bom.gov.au/nsw/forecasts/richmond.shtml')

#If chance of rain < 40% "Great day for the bike!
else:
    print('''      ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;''' + "\n\n The chance of rain is %s today, so it looks like you're in the clear!" % rain_chance + '''\n\n The forecast is: %s\n\n''' % for_sum)