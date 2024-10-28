import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:developer';

// final address = "https://81e9-220-117-157-36.ngrok-free.app";
final address = "https://spotty-radios-beam.loca.lt/";

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<StatefulWidget> createState() {
    return MyAppState();
  }
}

class MyAppState extends State<MyApp> {
  String result = '';

  onPressGet() async {
    Map<String, String> headers = {
      "content-type": "application/json",
      "accept": "application/json",
      "ngrok-skip-browser-warning": '0',
      "bypass-tunnel-reminder": '0'
    };
    http.Response response =
        await http.get(Uri.parse(address), headers: headers);
    if (response.statusCode == 200) {
      setState(
        () {
          result = utf8.decode(response.bodyBytes);
        },
      );
    } else {
      log('Error fetching data: ${response.statusCode}', name: 'GET Request');
    }
  }

  onPressPost() async {
    try {
      Map<String, String> body = {'name': '그루001', 'note': '플러터테스트'};
      http.Response response = await http.post(
        Uri.parse("$address/create"),
        headers: {'Content-Type': 'application/json'},
        body: json.encode(body),
      );
      if (response.statusCode == 200 || response.statusCode == 201) {
        setState(() {
          result = response.body;
        });
      } else {
        log('Error creating data: ${response.statusCode}',
            name: 'POST Request');
      }
    } catch (e) {
      log('Error occurred: $e', name: 'POST Request');
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      appBar: AppBar(
        title: Text('Test'),
      ),
      body: Center(
          child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(result),
          ElevatedButton(onPressed: onPressGet, child: Text('GET')),
          ElevatedButton(onPressed: onPressPost, child: Text('POST')),
        ],
      )),
    ));
  }
}
