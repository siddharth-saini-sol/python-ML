import 'dart:convert';


void main(){
  String j_son = '{"name":"siddahrth","age":19,"class":"t5"}';
  Map<String,dynamic> objson = jsonDecode(j_son);
  print(objson['name']);
  print(objson['age']);
}