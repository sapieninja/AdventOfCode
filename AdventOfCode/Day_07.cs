using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using AoCHelper;
using System.IO;
using System.Linq;

namespace AdventOfCode
{
    public class Day_07 : BaseDay
    {
        private static List<string> _input;
        private static List<Tuple<string,string,int>> _tuples = new List<Tuple<string, string,int>>();
        private static Dictionary<string,HashSet<string>> cache = new Dictionary<string, HashSet<string>>();

        public Day_07()
        {
            _input = File.ReadLines(InputFilePath).ToList();
        }

        public static HashSet<string> OneUp(string input,bool down = false)
        {
            //if (cache.ContainsKey(input)) return cache[input];
            var toReturn = new HashSet<string>();
            foreach (var tuple in _tuples)
            {
                if (down == false)
                {
                    if (tuple.Item1 == input)
                    {
                        toReturn.Add(tuple.Item2);
                    }
                }
                else
                {
                    if (tuple.Item2 == input)
                    {
                        toReturn.Add(tuple.Item1);
                    }
                }
            }

            //cache[input] = toReturn;
            return toReturn;
        }

        public static List<Tuple<int, string>> OneDown(string input)
        {
            var toReturn = new List<Tuple<int, string>>();
            foreach (var tuple in _tuples)
            {
                if (tuple.Item2 == input)
                {
                    toReturn.Add(new Tuple<int, string>(tuple.Item3,tuple.Item1));
                }
            }

            return toReturn;
        }
        public static string FindBags(bool part2 = false)
        {    
            _tuples = new List<Tuple<string, string, int>>();
            int start = 5;
            HashSet<string> PossibileSet = new HashSet<string>();
            List<string> words = new List<string>();
            foreach (var line in _input)
            {
                words = line.Split(" ", StringSplitOptions.RemoveEmptyEntries).ToList();
                if (words[4] == "no") continue;
                for (int i = 0; i < line.Count(x => x == ',') + 1 ; i++)
                {
                    var newTuple = new Tuple<string, string,int>(words[5+i*4] + words[6+i*4],words[0] + words[1],Convert.ToInt32(words[4+i*4]));
                    _tuples.Add(newTuple);
                }
            }

            const string toFind = "shinygold";
            if (!part2)
            {
                PossibileSet.UnionWith(OneUp(toFind));
                var AdditionSet = new HashSet<string>();
                int count = 0;
                while (true)
                {
                    foreach (var possible in PossibileSet)
                    {
                        AdditionSet.UnionWith(OneUp(possible));
                    }

                    PossibileSet.UnionWith(AdditionSet);
                    if (count == PossibileSet.Count())
                    {
                        break;
                    }
                    else
                    {
                        count = PossibileSet.Count();
                    }
                }

                return PossibileSet.Count.ToString();
            }
            else
            {
                int sum = 0;
                int oldsum = 0;
                List<Tuple<int, string>> nextTupleList = new List<Tuple<int, string>>();
                List<Tuple<int, string>> additionTupleList = new List<Tuple<int, string>>();
                var amounts = OneDown(toFind);
                while (true)
                {
                    nextTupleList = new List<Tuple<int, string>>();
                    foreach (var value in amounts)
                    {
                        sum += value.Item1;
                        additionTupleList = OneDown(value.Item2).ToList();
                        for (int i = 0; i<additionTupleList.Count;i++)
                        {
                            additionTupleList[i] = new Tuple<int, string>(additionTupleList[i].Item1*value.Item1,additionTupleList[i].Item2);
                        }

                        nextTupleList = nextTupleList.Concat(additionTupleList).ToList();
                    }

                    if (oldsum == sum) return sum.ToString();
                    oldsum = sum;
                    amounts = nextTupleList;
                }
            }

            return "";
        }

        public override string Solve_1()
        {
            return FindBags();
        }

        public override string Solve_2()
        {
            return FindBags(true);
        }
    }
}