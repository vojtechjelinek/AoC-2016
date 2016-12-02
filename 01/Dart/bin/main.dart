import 'dart:io';
import 'dart:math';

const north = const Point(0, 1);
const east = const Point(1, 0);
const south = const Point(0, -1);
const west = const Point(-1, 0);
List<Point> directions = const [north, east, south, west];

num taxicabDistance(Point pos) => (pos.x - pos.y).abs();

void main() {
  File file = new File('slepice.txt');
  String instructionsText = file.readAsStringSync();
  final List<String> instructions = instructionsText.split(", ");

  List<Point> visited = [];
  bool foundFirstIntersection = false;
  num direction = 0;
  Point position = new Point(0, 0);
  for (var instruction in instructions) {
    if (instruction[0] == 'R') {
      direction = (direction + 1) % 4;
    } else {
      direction = (direction - 1) % 4;
    }

    num steps = num.parse(instruction.substring(1));
    for (num i = 0; i < steps; i++) {
      position += directions[direction];
      if (visited.contains(position) && !foundFirstIntersection) {
        foundFirstIntersection = true;
        print("Distance of first intersection: ${taxicabDistance(position)}");
      }
      visited.add(position);
    }
  }

  print("Distance of end position: ${taxicabDistance(position)}");
}
