import 'package:flutter/material.dart';
import 'package:makeaton_client/screens/challenges.dart';
import 'package:makeaton_client/screens/community.dart';
import 'package:makeaton_client/screens/shopScreen.dart';

enum Options { challenge, community, shop }

class ChallengeCard extends StatelessWidget {
  const ChallengeCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Card(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          child: Container(
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20),
                image: DecorationImage(
                    image: NetworkImage(
                        'https://www.cater4you.co.uk/blog/wp-content/uploads/2018/08/huhtamaki-enjoy-12oz-coffee-cups-1000.jpg'),
                    fit: BoxFit.cover)),
            child: Container(
              padding: EdgeInsets.all(8),
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  gradient: LinearGradient(colors: [
                    Colors.red.withOpacity(0.2),
                    Colors.red.withOpacity(0.7)
                  ], begin: Alignment.topCenter, end: Alignment.bottomCenter)),
              child: Column(
                children: [
                  SizedBox(
                    height: 50,
                  ),
                  Text(
                    "Paper Cup Challenge is #trending now!",
                    style: TextStyle(fontSize: 30, color: Colors.white),
                  ),
                  SizedBox(
                    height: 5,
                  ),
                ],
              ),
            ),
          ),
        ),
        Align(
            alignment: Alignment.bottomRight,
            child: Text("Discover More  ",
                style: TextStyle(color: Colors.red[400], fontSize: 20))),
      ],
    );
  }
}

class OptionCard extends StatelessWidget {
  final Options opt;
  const OptionCard(this.opt, {Key? key}) : super(key: key);

  final Map<Options, String> titles = const {
    Options.community: "Community",
    Options.challenge: "Challenges",
    Options.shop: "Green Shop"
  };

  final Map<Options, String> desc = const {
    Options.community: "Find your Likeminded..",
    Options.challenge: "Take up a challenge",
    Options.shop: "Buy something green"
  };

  final Map<Options, String> images = const {
    Options.community: 'assets/community.png',
    Options.challenge: 'assets/challenge.png',
    Options.shop: 'assets/shop.png',
  };

  @override
  Widget build(BuildContext context) {
    return Center(
      child: AspectRatio(
        aspectRatio: 1,
        child: InkWell(
          onTap: () {
            if (opt == Options.challenge)
              Navigator.of(context)
                  .push(MaterialPageRoute(builder: (context) => Challenges()));
            else if (opt == Options.community)
              Navigator.of(context)
                  .push(MaterialPageRoute(builder: (context) => Community()));
            else if (opt == Options.shop)
              Navigator.of(context)
                  .push(MaterialPageRoute(builder: (context) => ShopScreen()));
          },
          child: Card(
            child: Container(
              padding: EdgeInsets.all(8),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        SizedBox(
                            height: 35,
                            width: 35,
                            child: Image.asset(
                              images[opt]!,
                            )),
                        Icon(Icons.arrow_forward_ios)
                      ]),
                  // Spacer(),
                  Text(titles[opt]!,
                      textAlign: TextAlign.left,
                      style: TextStyle(color: Colors.black87, fontSize: 20)),
                  // Spacer(),
                  Text(desc[opt]!,
                      textAlign: TextAlign.left,
                      style: TextStyle(color: Colors.black54, fontSize: 15)),
                  // Spacer(),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class SurveyCard extends StatelessWidget {
  const SurveyCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Container(
        child: Column(
          children: [
            Text("Paper Cup Challenge is #trending now!"),
            Text("Discover Challenges"),
          ],
        ),
      ),
    );
  }
}

class PromotionCard extends StatelessWidget {
  const PromotionCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Container(
        child: Column(
          children: [
            Text("Paper Cup Challenge is #trending now!"),
            Text("Discover Challenges"),
          ],
        ),
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("App NAME CO."),
        foregroundColor: Colors.black,
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: Container(
        padding: const EdgeInsets.all(18.0),
        decoration: BoxDecoration(
            image: DecorationImage(
                fit: BoxFit.fitWidth,
                alignment: Alignment.topCenter,
                image: AssetImage('assets/backg.png'))),
        child: Column(
          children: [
            // Expanded(
            //   child: GridView.count(
            //     crossAxisCount: 2,
            //     mainAxisSpacing: 10,
            //     crossAxisSpacing: 10,
            //     children: [
            //       Container(),
            Row(
              children: const [
                Expanded(
                    child: Text(
                  "Let's Go Green!",
                  style: TextStyle(fontSize: 40, color: Colors.black87),
                )),
                Expanded(child: OptionCard(Options.challenge)),
              ],
            ),
            Row(
              children: const [
                Expanded(child: OptionCard(Options.community)),
                Expanded(child: OptionCard(Options.shop)),
              ],
            ),
            //     ],
            //   ),
            // ),
            ChallengeCard(),
          ],
        ),
      ),
    );
  }
}
