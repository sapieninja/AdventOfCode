using System;
using System.Collections.Generic;
using System.ComponentModel;
using AoCHelper;
using System.IO;
using System.Linq;
using System.Windows.Markup;

namespace AdventOfCode
{
    public class Day_06 : BaseDay
    {
        private static string _input;

        public Day_06()
        {
            _input = File.ReadAllText(InputFilePath);
        }

        public static string Findnumber(bool solutionTwo = false)
        {
            var inputList = _input.Split("\n\n",
                StringSplitOptions.RemoveEmptyEntries).ToList();
            var contains = new HashSet<char>();
            int sum = 0;
            foreach (var group in inputList)
            {
                foreach (var value in group.Split("\n"))
                {
                    foreach (var character in value)
                    {
                        contains.Add(character);
                    }
                }

                if (!solutionTwo) sum += contains.Count;
                else
                {
                    foreach (var character in contains)
                    {
                        if (group.Count(e => e == character) == group.Split("\n").Count()) sum++;
                    }
                }
                contains = new HashSet<char>();
            }
            

            return sum.ToString();
        }

        public override string Solve_1()
        {
            return Findnumber();
        }

        public override string Solve_2()
        {
            return Findnumber(true);
        }
    }
}