#include <stdio.h>
#include <cs50.h>

int positive_input(string prompt)
{
    int n;
    do
    {
        n = get_int("%s", prompt);
    }
    while (n < 1 || n > 8);
    return n;
}

int main(void)
{

    int number_of_rows = positive_input("Height: ");
    for (int row_no = 0; row_no < number_of_rows; row_no++)
    {
        for (int dots = 0 ; dots < (number_of_rows - 1) - row_no; dots++)
            printf(" ");
        for (int hashes = 0; hashes < (row_no + 1); hashes++)
            printf("#");
        printf("  ");
        for (int other_hash = 0; other_hash < (row_no + 1); other_hash++)
            printf("#");
        printf("\n");
    }

}
