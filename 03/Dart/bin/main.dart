import 'dart:io';
import 'dart:math';
import 'dart:convert';

void main() {
  File file = new File('slepice.txt');
  String trianglesText = file.readAsStringSync();
  print(validTrianglesByLines(trianglesText));
  //print(validTrianglesByColumns(trianglesText));
}

num validTrianglesByLines(String text) {
  num validTriangles = 0;
  List<String> lines = new LineSplitter().convert(text);
  for (var line in lines) {
    List<num> sizes = [];
    sizes.add(num.parse(line.substring(0,5)));
    sizes.add(num.parse(line.substring(5,10)));
    sizes.add(num.parse(line.substring(10,15)));
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
  for (var line in lines) {
    List<num> sizes = [];
    sizes.add(num.parse(line.substring(0,5)));
    sizes.add(num.parse(line.substring(5,10)));
    sizes.add(num.parse(line.substring(10,15)));
    sizes.sort();
    if (sizes[0] + sizes[1] > sizes[2]) {
      validTriangles++;
    }
  }
  return validTriangles;
}
