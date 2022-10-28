import 'dart:convert';
import 'dart:io';

import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:http/http.dart';
import 'package:makeaton_client/insightsPopup.dart';

class CameraScreen extends StatefulWidget {
  const CameraScreen({Key? key}) : super(key: key);

  @override
  State<CameraScreen> createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen>
    with WidgetsBindingObserver {
  CameraController? controller;
  String? imageLabel = '', funFact = '', listFacts = '', listAlt = '';
  bool isBottomSheetUp = false;

  List<CameraDescription> _cameras = <CameraDescription>[];
  void initialiseCamera() async {
    try {
      WidgetsFlutterBinding.ensureInitialized();
      _cameras = await availableCameras();
      print("cameras got ${_cameras.length}");
      onNewCameraSelected(_cameras[0]);
    } on CameraException catch (e) {
      print("${e.code}, ${e.description}");
    }
  }

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    initialiseCamera();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    print("ivide");
    final CameraController? cameraController = controller;
    // App state changed before we got the chance to initialize.
    if (cameraController == null || !cameraController.value.isInitialized) {
      return;
    }

    if (state == AppLifecycleState.inactive) {
      cameraController.dispose();
    } else if (state == AppLifecycleState.resumed) {
      onNewCameraSelected(cameraController.description);
    }
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          _cameraPreviewWidget(),
          SafeArea(
            child: Align(
                alignment: Alignment.topCenter,
                child: SizedBox(
                  height: 70,
                  child: _pushButtonsRowWidget(),
                )),
          ),
          Align(
              alignment: Alignment.bottomCenter,
              child: _captureControlRowWidget()),
        ],
      ),
    );
  }

  /// Display the preview from the camera (or a message if the preview is not available).
  Widget _cameraPreviewWidget() {
    final CameraController? cameraController = controller;

    if (cameraController == null || !cameraController.value.isInitialized) {
      return const Text(
        'Finding Your Camera...',
        style: TextStyle(
          color: Colors.white,
          fontSize: 24.0,
          fontWeight: FontWeight.w900,
        ),
      );
    } else {
      return CameraPreview(
        controller!,
      );
    }
  }

  Widget _pushButtonsRowWidget() {
    return Row(
      children: [
        // Text(
        //   '  App NAME',
        //   style: TextStyle(color: Colors.white, fontSize: 25),
        // ),
        Spacer(),
        InkWell(
          onTap: () {},
          child: SizedBox(
              height: 30,
              width: 30,
              child: Image.asset('assets/community.png')),
        ),
        SizedBox(
          width: 20,
        ),
        InkWell(
          onTap: () {},
          child: SizedBox(
              height: 30, width: 30, child: Image.asset('assets/shop.png')),
        ),
        SizedBox(
          width: 20,
        ),
      ],
    );
  }

  bool loading = false;
  Widget _captureControlRowWidget() {
    final CameraController? cameraController = controller;

    return Padding(
      padding: const EdgeInsets.only(bottom: 20.0),
      child: SizedBox(
        height: 80,
        child: Center(
          child: InkWell(
              onTap: cameraController != null &&
                      cameraController.value.isInitialized &&
                      !loading
                  ? () async {
                      setState(() {
                        loading = true;
                      });
                      await onTakePictureButtonPressed();
                      if (imageLabel == null) {
                        setState(() {
                          loading = false;
                          return;
                        });
                      }
                      print(funFact);
                      print(isBottomSheetUp);
                      List<String> facts = [], alt = [];
                      for (String s in listFacts!.split('\n'))
                        if (s.trim() != '') facts.add(s);
                      for (String s in listAlt!.split('\n'))
                        if (s.trim() != '') alt.add(s);
                      print(facts);
                      print(alt);
                      setState(() {
                        loading = false;
                      });
                      if (isBottomSheetUp)
                        Navigator.of(context).pushReplacement(MaterialPageRoute(
                            builder: (context) => Insights(imageLabel ?? "Cat",
                                facts: facts, alts: alt)));
                    }
                  : null,
              child: Container(
                height: 70,
                decoration: const BoxDecoration(
                    shape: BoxShape.circle, color: Colors.white),
                child: Container(
                    margin: EdgeInsets.all(2),
                    decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        border: Border.all(color: Colors.grey[850]!, width: 2)),
                    child: loading
                        ? Center(
                            child: CircularProgressIndicator(
                              color: Colors.black,
                            ),
                          )
                        : Container()),
              )),
        ),
      ),
    );
  }

  Future onTakePictureButtonPressed() async {
    await takePicture().then((String? file) async {
      if (mounted) {
        if (file != null) {
          Map m = await getInsights(file);
          listAlt = m['list_of_alternatives'];
          listFacts = m['list_of_facts'];
          funFact = m['fun-facts'];
          isBottomSheetUp = true;
          setState(() {
            imageLabel = file;
          });
        }
      }
    });
  }

  Future<Map> getInsights(String img) async {
    try {
      Uri uri = Uri.parse("http://10.0.2.2:8000/api/insights/$img/");

      //content type application/json
      Map<String, String> headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer b39d8c48e78275c0b3be78547d2417f60f5581c6"
      };
      // make post request
      Response response = await get(uri, headers: headers);
      // check the status code for the result
      int statusCode = response.statusCode;
      print(response.body);
      if (statusCode == 200) {
        Map result = jsonDecode(response.body);
        return result;
      }

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
    return {
      "fun-facts": "\n.",
      "list_of_facts": "\n-",
      "list_of_alternatives": "\n"
    };
  }

  Future<String?> takePicture() async {
    final CameraController? cameraController = controller;
    if (cameraController == null || !cameraController.value.isInitialized) {
      print('Error: select a camera first.');
      return null;
    }

    if (cameraController.value.isTakingPicture) {
      return null;
    }

    try {
      final XFile file = await cameraController.takePicture();
      File f = File(file.path);
      List<int> fileInByte = f.readAsBytesSync();
      String fileInBase64 = base64Encode(fileInByte);
      return await detectObject(fileInBase64);
    } on CameraException catch (e) {
      print(e);
      return null;
    }
  }

  Future<String> detectObject(String image) async {
    try {
      Uri uri = Uri.parse("http://10.0.2.2:8000/api/detect/");

      //content type application/json
      Map<String, String> headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer b39d8c48e78275c0b3be78547d2417f60f5581c6"
      };
      Map body = {"image": image};
      // make post request
      Response response =
          await post(uri, headers: headers, body: jsonEncode(body));
      // check the status code for the result
      int statusCode = response.statusCode;
      print(response.body);
      if (statusCode == 200) {
        Map result = jsonDecode(response.body);
        return result['label'] ?? "Chair";
      }

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
    return image;
  }

  Future<void> onNewCameraSelected(CameraDescription cameraDescription) async {
    final CameraController? oldController = controller;
    print("soo");
    if (oldController != null) {
      // `controller` needs to be set to null before getting disposed,
      // to avoid a race condition when we use the controller that is being
      // disposed. This happens when camera permission dialog shows up,
      // which triggers `didChangeAppLifecycleState`, which disposes and
      // re-creates the controller.
      controller = null;
      await oldController.dispose();
    }

    final CameraController cameraController = CameraController(
      cameraDescription,
      ResolutionPreset.medium,
      imageFormatGroup: ImageFormatGroup.jpeg,
    );
    print(cameraController.value);
    // If the controller is updated then update the UI.
    cameraController.addListener(() {
      if (mounted) {
        setState(() {});
      }
      if (cameraController.value.hasError) {
        print('Camera error ${cameraController.value.errorDescription}');
      }
    });
    controller = cameraController;

    try {
      await cameraController.initialize();
    } on CameraException catch (e) {
      print('Error initializing camera: $e');
    }

    if (mounted) {
      setState(() {});
    }
  }
}
