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

let LoadPosts = () => {
  $(".Posts").find(".Post").remove()

  ReadAllPosts().done((data) => {
    var Posts = data.Response.Posts;

    Posts.reverse()

    for (var i = 0; i < Posts.length; i++) {
      let Post = Posts[i];

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
              <p>${Post.postText}</p>
            </div>
          </div>
        </div>
      `);
    }
  });
}


$(document).ready(() => {
  $("#Upload").click(() => {

    CreatePost($("#PostText").val(), $("#UserID").val())
    $("#PostText").val("")
    LoadPosts()

  });

  LoadPosts()
});
