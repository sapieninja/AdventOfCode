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
            HashSet<char> contains;
            int sum = 0;
            foreach (var group in inputList)
            {
                contains = new HashSet<char>(group.Split("\n").Select(e=>e.ToCharArray()).SelectMany(x => x));
                
                if (!solutionTwo) sum += contains.Count;
                else
                {
                    foreach (var character in contains)
                    {
                        if (group.Count(e => e == character) == group.Split("\n").Count()) sum++;
                    }
                }
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