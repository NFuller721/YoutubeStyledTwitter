let LoadPosts = () => {
  $(".Posts").find(".Post").remove()

  ReadAllPosts().done((data) => {
    var Posts = data.Response.Posts;


    Posts.reverse()

    for (var i = 0; i < Posts.length; i++) {
      let Post = Posts[i];
      let ShouldBeIncluded = false;

      let TextArray = Post.postText.split(" ")

      var LinkText = "";
      var Hashtags = "";
      var TextArrayWithoutLinks = [];

      for (var j = 0; j < TextArray.length; j++) {
        let Word = TextArray[j];

        if (Word.slice(0,7) == "http://" || Word.slice(0,8) == "https://") {
          LinkText = LinkText.concat(`<a href="${Word}">${Word}</a>`)
        } else if (Word.slice(0,1) == "#") {
          if (Word == Hashtag) {
            ShouldBeIncluded = true;
          }
          Hashtags = Hashtags.concat(`<a href="/Hashtags/${Word.slice(1)}">${Word}</a>`)
        } else {
          TextArrayWithoutLinks.push(Word);
        }
      }

      LinkText = LinkText != "" ? LinkText.concat("<br />") : ""

      var EllipsisBox = ""

      if (deletablePosts.includes(Post.id)) {
        EllipsisBox = `
        <div class="Ellipsis">
          <input type='image' onclick="Ellipsis(${Post.id})" src="https://img.icons8.com/ios-filled/24/303030/ellipsis.png"/>
          <div class='optionsBox' id="${Post.id}">
            <input type="button" onclick="DeletePostButton(${Post.id})" value="Delete">
          </div>
        </div>
        `
      } else {
        EllipsisBox = ``
      }
      if (ShouldBeIncluded) {

        $(".Posts").append(`
          <div class="Post">
            <div class="UserPicture">
              <img id="img" class="style-scope yt-img-shadow" alt="Avatar image" height="32" width="32" src="${Post.userPicture}">
            </div>
              <div class="PostContent">
              <div class="PostUsername">
              <p>${Post.userName}</p>
            </div>
              <div class="PostText">
                <p>${TextArrayWithoutLinks.join(" ")}</p>
                ${LinkText}
                ${Hashtags}
              </div>
            </div>
            ${EllipsisBox}
          </div>
          `);
      }
    }
  });
}


$(document).ready(() => {
  LoadPosts()
});
