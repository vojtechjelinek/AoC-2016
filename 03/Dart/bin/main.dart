import 'dart:io';
import 'dart:convert';

const north = const Point(0, 1);
const east = const Point(1, 0);
const south = const Point(0, -1);
const west = const Point(-1, 0);
List<Point> directions = const [north, east, south, west];

void main() {
  File file = new File('slepice.txt');
  String trianglesText = file.readAsStringSync();
  print(validTrianglesByLines(trianglesText));
  print(validTrianglesByColumns(trianglesText));
}

num validTrianglesByLines(String text) {
  num validTriangles = 0;
  List<String> lines = new LineSplitter().convert(text);
  for (var line in lines) {
    List<num> sizes = [];
    sizes.add(num.parse(line.substring(0, 5)));
    sizes.add(num.parse(line.substring(5, 10)));
    sizes.add(num.parse(line.substring(10, 15)));
    sizes.sort();
    if (sizes[0] + sizes[1] > sizes[2]) {
      validTriangles++;
    }
  }
  return validTriangles;
}

num validTrianglesByColumns(String text) {
  num validTriangles = 0;
  List<String> lines = new LineSplitter().convert(text);
  num i = 0;
  List<List<num>> sizes = [[], [], []];
  for (var line in lines) {
    sizes[0].add(num.parse(line.substring(0, 5)));
    sizes[1].add(num.parse(line.substring(5, 10)));
    sizes[2].add(num.parse(line.substring(10, 15)));
    if (++i == 3) {
      i = 0;
      for (var j = 0; j < 3; j++) {
        sizes[j].sort();
        if (sizes[j][0] + sizes[j][1] > sizes[j][2]) {
          validTriangles++;
        }
      }
      sizes = [[], [], []];
    }
  }
  return validTriangles;
}
