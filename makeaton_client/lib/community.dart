import 'package:awesome_icons/awesome_icons.dart';
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Data_Model_Story {
  final String name;
  final String profilepic;
  final String postphoto;

  Data_Model_Story(
      {required this.name, required this.profilepic, required this.postphoto});
}

// dummy data to show Profile post and story image and Name of the account user.
List<Data_Model_Story> dummyStoryData = [
  Data_Model_Story(
      name: "Rajat Palankar",
      postphoto:
          "https://th.bing.com/th/id/OIP.tdXb6nJWuf9OEehKfOLrHwHaHQ?pid=ImgDet&w=736&h=722&rs=1",
      profilepic:
          "https://th.bing.com/th/id/OIP.tdXb6nJWuf9OEehKfOLrHwHaHQ?pid=ImgDet&w=736&h=722&rs=1"),
  Data_Model_Story(
      name: "BB ki Vines",
      postphoto:
          "https://i.gadgets360cdn.com/large/bb_ki_vines_body_1579760395127.jpg",
      profilepic:
          "https://images-na.ssl-images-amazon.com/images/I/711q+ma1FQL.png"),
  Data_Model_Story(
      name: "ashishchanchlani",
      postphoto:
          "https://assets.entrepreneur.com/content/3x2/2000/20200217104953-Ashish1.jpeg",
      profilepic:
          "https://yt3.ggpht.com/a/AATXAJwZGPuuePGI6Mr887w6f6ZxsnoDl-Xf10gKPKIOeg=s900-c-k-c0xffffffff-no-rj-mo"),
  Data_Model_Story(
      name: "  Angry Prash",
      postphoto: "https://pbs.twimg.com/media/D1tL281XcAAAAd1.jpg",
      profilepic:
          "https://pbs.twimg.com/profile_images/1143239373489463296/Zv3BvjsA.jpg"),
  Data_Model_Story(
      name: "carryminati",
      postphoto: "https://i.ytimg.com/vi/zzwRbKI2pn4/maxresdefault.jpg",
      profilepic:
          "https://m.media-amazon.com/images/M/MV5BM2NlNzUyODUtZDgyNS00ZjU3LWI5NGUtOWFkYmQwMGVlNGRmXkEyXkFqcGdeQXVyMTE2MTc3MzU1._V1_.jpg"),
  Data_Model_Story(
      name: "Leo",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2016/11/29/02/28/attractive-1866858__340.jpg"),
  Data_Model_Story(
      name: "Jack",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2017/06/26/02/47/people-2442565__340.jpg"),
  Data_Model_Story(
      name: "Amelia",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2018/01/24/19/49/people-3104635__340.jpg"),
  Data_Model_Story(
      name: "Sophia",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2017/11/23/07/47/babe-2972221__340.jpg"),
  Data_Model_Story(
      name: "Harry",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2018/02/21/15/06/woman-3170568__340.jpg"),
  Data_Model_Story(
      name: "Isla",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2016/01/19/18/04/man-1150058__340.jpg"),
  Data_Model_Story(
      name: "Emily",
      postphoto:
          "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
      profilepic:
          "https://cdn.pixabay.com/photo/2015/07/31/15/01/man-869215__340.jpg"),
];

class InstaList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var deviceSize = MediaQuery.of(context).size;
    return ListView.builder(
      itemCount: dummyStoryData.length,
      itemBuilder: (context, index) => Column(
        mainAxisAlignment: MainAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          //1st row

          Padding(
            padding: const EdgeInsets.fromLTRB(16.0, 16.0, 8.0, 16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    Container(
                      height: 40.0,
                      width: 40.0,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        image: DecorationImage(
                            fit: BoxFit.fill,
                            image:
                                NetworkImage(dummyStoryData[index].profilepic)),
                      ),
                    ),
                    SizedBox(
                      width: 10.0,
                    ),
                    Text(
                      dummyStoryData[index].name,
                      style: TextStyle(fontWeight: FontWeight.bold),
                    ),
                  ],
                ),
                IconButton(
                  icon: Icon(Icons.more_vert),
                  onPressed: null,
                )
              ],
            ),
          ),

          //2nd row

          InteractiveViewer(
            boundaryMargin: EdgeInsets.all(8.0),
            minScale: 0.1,
            maxScale: 1.6,
            onInteractionUpdate: (_) => print("Interaction Updated"),
            child: Image.network(
              dummyStoryData[index].postphoto,
              fit: BoxFit.cover,
            ),

            // ),
          ),

          //3rd row

          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: const [
                    Icon(FontAwesomeIcons.heart),
                    SizedBox(
                      width: 10,
                    ),
                    Icon(FontAwesomeIcons.comment),
                    SizedBox(
                      width: 10,
                    ),
                    Icon(FontAwesomeIcons.paperPlane)
                  ],
                ),
                Icon(FontAwesomeIcons.bookmark)
              ],
            ),
          ),

          //4th Row

          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0),
            child: Text(
              "Liked by Rajat Palankar and 568,444 others ",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
          ),

          //5th Row

          Padding(
            padding: const EdgeInsets.fromLTRB(16.0, 16.0, 8.0, 8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Container(
                  height: 40.0,
                  width: 40.0,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    image: DecorationImage(
                        fit: BoxFit.fill,
                        image: NetworkImage(dummyStoryData[index].profilepic)),
                  ),
                ),
                SizedBox(
                  width: 10.0,
                ),
                Expanded(
                  child: TextField(
                    decoration: InputDecoration(
                        border: InputBorder.none, hintText: "Add a comment..."),
                  ),
                )
              ],
            ),
          ),

// 6th row
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0),
            child: Text(
              "20 Minutes Ago",
              style: TextStyle(color: Colors.grey),
            ),
          )
        ],
      ),
    );
  }
}

class Community extends StatelessWidget {
  const Community({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        foregroundColor: Colors.black,
        elevation: 0,
        title: Text('Community'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Flexible(
            child: InstaList(),
          )
        ],
      ),
    );
  }
}
