class Info {
  final String username;
  final String email;
  final String password;
  final String gender;
  final String login_token;

  const Info({
    required this.username,
    required this.email,
    required this.password,
    required this.gender,
    required this.login_token,
  });

  static Info fromJson(json) => Info(
        username: json['name'],
        email: json['floor_price'],
        password: json['new_url'],
        gender: json['url'],
        login_token: json['metadata'],
      );
}
