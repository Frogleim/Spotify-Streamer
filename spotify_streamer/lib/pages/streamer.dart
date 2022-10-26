import 'package:any_link_preview/any_link_preview.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:spotify_streamer/models/accounts_models.dart';
import 'package:spotify_streamer/API/api.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class NFT_page extends StatefulWidget {
  const NFT_page({super.key});

  @override
  State<NFT_page> createState() => _NFT_pageState();
}

class _NFT_pageState extends State<NFT_page> {
  final String _url =
      'https://www.youtube.com/results?search_query=link+preview+flutter';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Card(
          child: FutureBuilder(
            future: getInfoData(),
            builder: (context, snapshot) {
              if (snapshot.data == null) {
                return Container(child: Center(child: Text('Loading')));
              } else {
                return ListView.builder(
                  itemBuilder: (context, index) {
                    return ListTile(
                      title: Text(snapshot.data[index].name),
                      subtitle: Text(
                          'Floor price in opensea.io is ${snapshot.data[index].email}\nMagiceden.io '),
                    );
                  },
                  itemCount: snapshot.data.length,
                );
              }
            },
          ),
        ),
      ),
    );
  }
}
