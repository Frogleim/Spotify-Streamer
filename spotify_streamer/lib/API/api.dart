import 'package:spotify_streamer/models/accounts_models.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

Future getInfoData() async {
  var response = await http.get(Uri.parse('http://10.0.2.2:50162/'));
  var jsonData = jsonDecode(response.body);
  List<Info> infos = [];
  for (var items in jsonData) {
    Info info = Info(
      username: items['name'],
      email: items['floor_price'],
      password: items['new_url'],
      gender: items['url'],
      login_token: items['metadata'],
    );
    infos.add(info);
  }
  print(infos.length);
  return infos;
}
