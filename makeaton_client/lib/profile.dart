import 'package:flutter/material.dart';
import 'package:gif/gif.dart';
import 'challenges.dart';
import 'community.dart';
import 'shopScreen.dart';

class GIFEg extends StatefulWidget {
  const GIFEg({Key? key}) : super(key: key);

  @override
  State<GIFEg> createState() => _GIFEgState();
}

class _GIFEgState extends State<GIFEg> with TickerProviderStateMixin {
  GifController? _controller;

  @override
  initState() {
    super.initState();
    _controller = GifController(vsync: this);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
      child: Gif(
        image: AssetImage("assets/thunder-lightning.gif"),

        controller:
            _controller, // if duration and fps is null, original gif fps will be used.
        //fps: 30,
        //duration: const Duration(seconds: 3),
        // autostart: Autostart.no,
        placeholder: (context) => const Text('Loading...'),
        onFetchCompleted: () {
          if (_controller != null) {
            _controller!.reset();
            _controller!.forward();
          }
        },
      ),
    ));
  }
}
