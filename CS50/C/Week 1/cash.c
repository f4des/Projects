#include <stdio.h>
#include <cs50.h>

float get_cash(string prompt)
{
    int n;
    do
    {
        n = get_float("%s", prompt);
    }
    while (n <= 0);
    return n;
}

int main(void)
{
    float quarter = 0.25;
    float dime = 0.1;
    float nickel = 0.05;
    float penny = 0.01;
    float cash = get_cash("Change Owed: ");





}
