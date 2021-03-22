let CreatePost = (postText, userID) => {
  $.post("/Api/34567654/CreatePost", {"postText": postText, "userID": userID}, (data) => {
    console.log(data);
  });
}
let ReadPost = (id) => {
  return $.post("/Api/34567654/ReadPost", {"id": id});
}
let ReadAllPosts = () => {
  return $.post("/Api/34567654/ReadAllPosts", {});
}
let UpdatePost = (id, postText) => {
  $.post("/Api/34567654/UpdatePost", {"id": id, "postText": postText}, (data) => {
    console.log(data);
  });
}
let DeletePost = (id) => {
  $.post("/Api/34567654/DeletePost", {"id": id}, (data) => {
    console.log(data);
  });
}
let DeleteAllPosts = (AdminUsername, AdminPassword) => {
  $.post("/Api/34567654/DeleteAllPosts", {"AdminUsername": AdminUsername, "AdminPassword": AdminPassword}, (data) => {
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

let EditPostButton = (id) => {

  // Remove text
  $(`.PostText#Post-${id}`).find(".content").find("p").remove()

  // Define text in post
  let Text = $(`.PostText#Post-${id}`).find(".content").find("input:hidden").val()

  // Make input with value of Text
  $(`.PostText#Post-${id}`).find(".content").append(`<input type="text" value="${Text}">`)
  $(`.PostText#Post-${id}`).find(".content").append(`<input type="button" value="Update">`)
}

let EditPostSubmit = () => {

}

$(document).ready(() => {
  $(document).mouseup((e) => {
      var container = $(".optionsBox");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
          container.hide();
      }
  });
});
