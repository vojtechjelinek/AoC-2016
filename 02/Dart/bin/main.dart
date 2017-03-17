import 'dart:io';
import 'dart:convert';
import 'dart:math';

const up = const Point(0, -1);
const right = const Point(1, 0);
const down = const Point(0, 1);
const left = const Point(-1, 0);
Map<String, Point> directions = const {'U': up,
                                       'R': right,
                                       'D': down,
                                       'L': left};

main(List<String> args) {
  File file = new File('slepice.txt');
  String instructions = file.readAsStringSync();
  file = new File('map1.txt');
  final List<List<String>> map1 = parseMap(file.readAsStringSync());
  print(solve(instructions, map1));
  file = new File('map2.txt');
  final List<List<String>> map2 = parseMap(file.readAsStringSync());
  print(solve(instructions, map2));
}

List<List<String>> parseMap(String textMap) {
  List<List<String>> map = [];
  List<String> lines = new LineSplitter().convert(textMap);
  num buttonsInLine = (lines[0].length + 1) ~/ 2 + 2;
  map.add(new List.filled(buttonsInLine, "#"));
  for (var line in lines) {
    List<String> mapLine = [];
    mapLine.add('#');
    mapLine.addAll(line.split(' '));
    mapLine.add('#');
    map.add(mapLine);
  }
  map.add(new List.filled(buttonsInLine, "#"));
  return map;
}

solve(String instructions, List<List<String>> map) {
  Point pos;
  String password = "";
  for (var i = 0; i < map.length; i++) {
    if (map[i].indexOf('5') >= 0) {
        pos = new Point(map[i].indexOf('5'), i);
    }
  }
  List<String> lines = new LineSplitter().convert(instructions);
  for (var line in lines) {
    for (var char in line.split('')) {
      Point newPos = pos + directions[char];
      if (map[newPos.y][newPos.x] != '#') {
        pos = newPos;
      }
    }
    password += map[pos.y][pos.x];
  }
  return password;
}
