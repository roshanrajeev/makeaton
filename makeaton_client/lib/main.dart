import "package:flutter/material.dart";
import "package:gif/gif.dart";
import "challenges.dart";
import "community.dart";
import "shopScreen.dart";

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Makeaton",
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Challenges(),
    );
  }
}
