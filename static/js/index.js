let CreatePost = (postText, userID) => {
  $.post("Api/34567654/CreatePost", {"postText": postText, "userID": userID}, (data) => {
    console.log(data);
  });
}

let ReadPost = (id) => {
  return $.post("Api/34567654/ReadPost", {"id": id});
}

let ReadAllPosts = () => {
  return $.post("Api/34567654/ReadAllPosts", {});
}

let UpdatePost = (id, postText) => {
  $.post("Api/34567654/UpdatePost", {"id": id, "postText": postText}, (data) => {
    console.log(data);
  });
}

let DeletePost = (id) => {
  $.post("Api/34567654/DeletePost", {"id": id}, (data) => {
    console.log(data);
  });
}

let DeleteAllPosts = (AdminUsername, AdminPassword) => {
  $.post("Api/34567654/DeleteAllPosts", {"AdminUsername": AdminUsername, "AdminPassword": AdminPassword}, (data) => {
    console.log(data);
  });
}

let Ellipsis = (id) => {
  $(`.optionsBox#${id}`).css("display", "block")
}

let DeletePostButton = (id) => {
  $(`.optionsBox#${id}`).css("display", "none")
  DeletePost(id)

  setTimeout(() => {
    LoadPosts()
  }, 175)
}

let LoadPosts = () => {
  $(".Posts").find(".Post").remove()

  ReadAllPosts().done((data) => {
    var Posts = data.Response.Posts;

    Posts.reverse()

    for (var i = 0; i < Posts.length; i++) {
      let Post = Posts[i];

      let TextArray = Post.postText.split(" ")

      var LinkText = "";
      var TextArrayWithoutLinks = [];

      for (var j = 0; j < TextArray.length; j++) {
        let Word = TextArray[j];

        if (Word.slice(0,7) == "http://" || Word.slice(0,8) == "https://") {
          LinkText = LinkText.concat(`<a href="${Word}">${Word}</a>`)
        } else {
          TextArrayWithoutLinks.push(Word);
        }
      }

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
            </div>
          </div>
          ${EllipsisBox}
        </div>
      `);
    }
  });
}


$(document).ready(() => {

  $(document).mouseup(function(e)
  {
      var container = $(".optionsBox");

      // if the target of the click isn't the container nor a descendant of the container
      if (!container.is(e.target) && container.has(e.target).length === 0)
      {
          container.hide();
      }
  });

  $("#Upload").click(() => {

    CreatePost($("#PostText").val(), $("#UserID").val())
    $("#PostText").val("")

    setTimeout(() => {
      LoadPosts()
    }, 175)

  });

  LoadPosts()
});
