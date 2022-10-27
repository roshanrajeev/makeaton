import 'package:flutter/material.dart';

class ChallengeCard extends StatelessWidget {
  const ChallengeCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 18, vertical: 9),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(
          "Paper Cup Challenge",
          style: TextStyle(fontSize: 19, fontWeight: FontWeight.bold),
        ),
        Row(
          children: [
            Expanded(
                child:
                    Text("Do not use any disposible cup for the next 7 days.")),
            TextButton(onPressed: () {}, child: Text("Let's Do It"))
          ],
        )
      ]),
    );
  }
}

class Challenges extends StatelessWidget {
  const Challenges({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("App NAME CO."),
          foregroundColor: Colors.black,
          backgroundColor: Colors.transparent,
          elevation: 0,
        ),
        body: ListView.builder(
          itemCount: 40,
          itemBuilder: (context, ind) {
            return ChallengeCard();
          },
        ));
  }
}
