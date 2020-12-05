using System;
using System.Collections.Generic;
using AoCHelper;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Threading;

namespace AdventOfCode
{
    public class Day_05 : BaseDay
    {
        private static List<string> _input;

        public Day_05()
        {
            _input = File.ReadLines(InputFilePath).ToList();
        }

        public static string solve(bool solution2 = false)
        {    
            var scores = new List<int>();
            int score = 0;
            string seatcode = "";
            foreach (var pass in _input)
            {
                seatcode = pass.Replace("B","1");
                seatcode = seatcode.Replace("F","0");
                seatcode = seatcode.Replace("R", "1");
                seatcode = seatcode.Replace("L", "0");
                score = Convert.ToInt32(seatcode, 2);
                scores.Add(score);
                //Now we look for a missing seat in every row
            }
            if (solution2 == true)
            {
                var missing = Enumerable.Range(1, 1024).Except(scores);
                int i = 1;
                foreach (var value in missing)
                {
                    if (i != value)
                    {
                        return value.ToString();
                    }

                    i++;
                }
            }

            return scores.Max().ToString();
        }
        

        public override string Solve_1()
        {
            return solve();
        }

        public override string Solve_2()
        {
            return solve(true);
        }
    }
}