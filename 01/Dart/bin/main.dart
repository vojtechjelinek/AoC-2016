import 'dart:io';
import 'dart:async';

void main() {
    var file = new File("slepice.txt");
    String instructions_text = file.readAsStringSync();
    List<String> instructions = instructions_text.split(", ");
}
