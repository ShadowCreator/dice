import std.stdio;
import std.random;
import std.conv;


void main(string[] args)
{
  int numberOfDice = to!int(args[1]);
  int sides = to!int(args[2]);
  int bonus = to!int(args[3]);
  auto randy = uniform(0, sides) + 1;
  int total = (numberOfDice * randy) + bonus;
  writeln(numberOfDice, "d", sides, "+", bonus, " = ", total);
}
