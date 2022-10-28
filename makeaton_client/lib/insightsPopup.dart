import 'package:flutter/material.dart';
import 'package:makeaton_client/cameraScreen.dart';
import 'package:makeaton_client/homePage.dart';

class Insights extends StatelessWidget {
  final String objectName;
  final List<String> facts, alts;
  const Insights(this.objectName,
      {this.facts = const [], this.alts = const [], super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
      decoration: BoxDecoration(
          image: DecorationImage(
              image: AssetImage('assets/background.jpg'), fit: BoxFit.cover)),
      child: Container(
        decoration: BoxDecoration(color: Color.fromARGB(220, 0, 1, 75)),
        child: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
                IconButton(
                  icon: Icon(Icons.camera_alt, color: Colors.white),
                  onPressed: () {
                    Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                            builder: (context) => CameraScreen()));
                  },
                ),
                TextButton(
                  onPressed: () {
                    Navigator.pushReplacement(context,
                        MaterialPageRoute(builder: (context) => HomeScreen()));
                  },
                  child: Text('Skip', style: TextStyle(color: Colors.white)),
                )
              ]),
              Expanded(
                flex: 5,
                child: Image.network(
                    'https://www.pngpix.com/wp-content/uploads/2016/07/PNGPIX-COM-Woden-Chair-PNG-Transparent-Image.png'),
              ),
              Expanded(
                  flex: 3,
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Text(
                          objectName.toUpperCase(),
                          style: TextStyle(
                              fontSize: 30,
                              color: Colors.white,
                              fontWeight: FontWeight.bold),
                        ),
                        // Divider(
                        //   height: 30,
                        //   thickness: 3,
                        // ),
                        Text(
                          facts[0][0] == '1'
                              ? facts[0].substring(3)
                              : facts[0].substring(1),
                          style: TextStyle(fontSize: 17, color: Colors.white),
                        ),
                        Text(
                          alts[0][0] == '1'
                              ? alts[0].substring(3)
                              : alts[0].substring(1),
                          style: TextStyle(
                              fontSize: 17,
                              fontWeight: FontWeight.w600,
                              color: Colors.white),
                        )
                      ],
                    ),
                  )),
              Expanded(
                flex: 3,
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Suggested Challenges',
                          style: TextStyle(fontSize: 20, color: Colors.white),
                        ),
                        SizedBox(height: 8),
                        Expanded(
                          child: ListView(
                            scrollDirection: Axis.horizontal,
                            children: [
                              Card(
                                child: Container(
                                  width: MediaQuery.of(context).size.width - 64,
                                  child: Row(
                                    children: [
                                      Padding(
                                        padding: const EdgeInsets.all(8.0),
                                        child: Image.network(
                                            'https://www.pngpix.com/wp-content/uploads/2016/07/PNGPIX-COM-Woden-Chair-PNG-Transparent-Image.png'),
                                      ),
                                      Expanded(
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceEvenly,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          children: const [
                                            Text(
                                              'Musical Chairs',
                                              style: TextStyle(
                                                fontSize: 20,
                                              ),
                                            ),
                                            Text(
                                              'Make a chair out of recycled materials',
                                              softWrap: true,
                                              overflow: TextOverflow.fade,
                                            ),
                                          ],
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              Card(
                                child: Container(
                                  width: MediaQuery.of(context).size.width - 64,
                                  child: Row(
                                    children: [
                                      Expanded(
                                        child: Padding(
                                          padding: const EdgeInsets.all(8.0),
                                          child: Image.network(
                                              'https://www.pngpix.com/wp-content/uploads/2016/07/PNGPIX-COM-Woden-Chair-PNG-Transparent-Image.png'),
                                        ),
                                      ),
                                      Expanded(
                                        flex: 3,
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceEvenly,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.stretch,
                                          children: [
                                            Text(
                                              'Musical Chairs',
                                              style: TextStyle(
                                                fontSize: 20,
                                              ),
                                            ),
                                            Text(
                                              'Make a recycled chair',
                                              // maxLines: 3,
                                              // softWrap: true,
                                              // overflow: TextOverflow.ellipsis,
                                            ),
                                          ],
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        )
                      ]),
                ),
              )
            ],
          ),
        ),
      ),
    ));
  }
}
