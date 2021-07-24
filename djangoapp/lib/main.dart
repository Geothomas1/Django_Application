import 'package:flutter/material.dart';
import 'package:djangoapp/services/SampleService.dart';
import 'package:djangoapp/utils/httpResponse.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // const Home({Key? key}) : super(key: key);
  _getresponse() async {
    HttpResponse? response = await sampleService.get();
    print(response);
  }

  SampleService sampleService = SampleService();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(
          child: Center(
            child: TextButton(
              child: Text('Click'),
              onPressed: _getresponse(),
            ),
          ),
        ),
      ),
    );
  }
}
