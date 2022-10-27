import 'package:flutter/material.dart';

class ProductModel {
  final String name;
  final String pic;
  final String description;

  ProductModel(
      {required this.name, required this.pic, required this.description});
}

List<ProductModel> products = [
  ProductModel(
      name: "Wooden Spoon and Fork Set",
      pic:
          'https://th.bing.com/th/id/OIP.X118PvhsGlV76qTA0HaE5AHaHa?pid=ImgDet&rs=1',
      description:
          'Disposible wooden utensils, suitable for events and functions.'),
  ProductModel(
      name: "Paper Pens",
      pic:
          'https://th.bing.com/th/id/OIP.X118PvhsGlV76qTA0HaE5AHaHa?pid=ImgDet&rs=1',
      description:
          'Green Pens, which gives the same feel as the normal pen, or even better!'),
  ProductModel(
      name: "Shampoo Bar",
      pic:
          'https://th.bing.com/th/id/OIP.X118PvhsGlV76qTA0HaE5AHaHa?pid=ImgDet&rs=1',
      description:
          'This shampoo bar could be used for ages, and even more if you bath rare.')
];

class ProductCard extends StatelessWidget {
  final ProductModel pdt;
  const ProductCard(this.pdt, {Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Row(children: [
        Expanded(
          child: Image.network(pdt.pic),
        ),
        Expanded(
          flex: 3,
          child: Column(children: [Text(pdt.name), Text(pdt.description)]),
        )
      ]),
    );
  }
}

class ShopScreen extends StatelessWidget {
  const ShopScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          foregroundColor: Colors.black,
          elevation: 0,
          title: Text('Community'),
        ),
        body: ListView.builder(
          itemBuilder: ((context, index) => ProductCard(products[index])),
          itemCount: products.length,
        ));
  }
}
