using System;
using System.Collections.Generic;
using AoCHelper;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;

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
            var seats = new List<(int row, int column)>();
            var row = 0;
            int score = 0;
            string start = "";
            string end = "";
            var column = 0;
            foreach (var pass in _input)
            {
                start = pass.Substring(0,7);
                start = start.Replace("B","1");
                start = start.Replace("F","0");
                row = Convert.ToInt32(start,2);
                end = pass.Substring(7,3);
                end = end.Replace("R","1");
                end = end.Replace("L","0");
                column = Convert.ToInt32(end, 2);
                score = row * 8 + column;
                scores.Add(score);
                //Now we look for a missing seat in every row
                seats.Add((row,column));
            }

            var doneRows = new List<int>();
            var columns = new List<int>();
            var sum = 0;

            if (solution2 == true)
            {
                foreach (var seat in seats)
                {
                    row = seat.row;
                    foreach (var subseat in seats)
                    {
                        if (subseat.row == row)
                        {
                            columns.Add(subseat.column);
                        }
                    }

                    if (columns.Count != 8)
                    {    
                        foreach (var columnvalue in columns)
                        {
                            sum += columnvalue;
                        }

                        if (sum != 28)
                        {
                            column = 28 - sum;
                            return (row * 8 + column).ToString();
                        }

                        sum = 0;
                    }
                    columns = new List<int>();
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