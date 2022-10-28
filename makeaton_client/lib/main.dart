import 'dart:convert';

import "package:flutter/material.dart";
import "package:gif/gif.dart";
import 'package:http/http.dart';
import 'package:makeaton_client/cameraScreen.dart';
import "challenges.dart";
import "community.dart";
import 'insightsPopup.dart';
import "shopScreen.dart";
import 'package:http/io_client.dart';
import 'dart:io';
// import 'package:http/http.dart';
import 'dart:async';
// import 'dart:convert';

// Future login() async {
//   Map inp = {"email": "roshan4@gmail.com", "password": "Roshan@123"};
//   print('noww');
//   Uri uri = Uri.parse("https://4c2d-42-104-154-90.in.ngrok.io/api/login/");
//   var response = await post(uri, body: inp);
//   print(response.body);
//   Map<String, String> result = jsonDecode(response.body);
// }
Future getAccessToken() async {
  try {
    Uri uri = Uri.parse("http://10.0.2.2:8000/api/login/");

    //content type application/json
    Map<String, String> headers = {
      "Content-type": "application/json",
    };
    // body
    Map<String, String> body = {
      "email": "roshan@gmail.com",
      "password": "Roshan@123"
    };
    // make post request
    Response response =
        await post(uri, headers: headers, body: jsonEncode(body));
    // check the status code for the result
    int statusCode = response.statusCode;
    print(response.body);

    // http.post(uri, body: {
    //   "email": "roshan4@gmail.com",
    //   "password": "Roshan@123"
    // }).then((response) {
    //   print("Reponse status : ${response.statusCode}");
    //   print("Response body : ${response.body}");
    //   var myresponse = jsonDecode(response.body);
    //   String token = myresponse["token"];
    // });
  } catch (e) {
    print(e.toString());
  }
}

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // login();
    getAccessToken();
    return MaterialApp(
        title: "Makeaton",
        theme: ThemeData(
          primarySwatch: Colors.blue,
          fontFamily: 'Montserrat',
          primaryTextTheme: TextTheme()
        ),
        home: CameraScreen());
        // Insights(
        //   "Cat",
        //   facts: ["Cat is Good"],
        //   alts: ["Replace with dog"],
        // ));
  }
}
