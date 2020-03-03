 $().ready(function() {
    // validate the comment form when it is submitted
    $("#commentForm").validate();

    // validate signup form on keyup and submit
    $("#signupForm").validate({
      rules: {
        firstname: "required",
        lastname: "required",
        username: {
          required: true,
          minlength: 6
        },
        password: {
          required: true,
          minlength: 8
        },
        confirm_password: {
          required: true,
          minlength: 8,
          equalTo: "#password"
        },
        email: {
          required: true,
          email: true
        },
        topic: {
          required: "#newsletter:checked",
          minlength: 2
        },
        agree: "required"
      },
      messages: {
        firstname: "Please enter your firstname",
        lastname: "Please enter your lastname",
        username: {
          required: "<span style='color:red;'>Please enter a username</span>",
          minlength: "<span style='color:red;'>username at least 6 characters</span>"
        },
        password: {
          required: "<span style='color:red;'>Please provide a password</span>",
          minlength: "<span style='color:red;'>password  at least 5 characters</span>"
        },
        confirm_password: {
          required: "<span style='color:red;'>Please provide a confirm password",
          minlength: "<span style='color:red;'>password at least 5 characters</span>",
          equalTo: "<span style='color:red;'>Please enter the same password as above</span>"
        },
        email: "Please enter a valid email address",
        agree: "Please accept our policy",
        topic: "Please select at least 2 topics"
      }
    });

    // propose username by combining first- and lastname
    $("#username").focus(function() {
      var firstname = $("#firstname").val();
      var lastname = $("#lastname").val();
      if (firstname && lastname && !this.value) {
        this.value = firstname + "." + lastname;
      }
    });

    //code to hide topic selection, disable for demo
    var newsletter = $("#newsletter");
    // newsletter topics are optional, hide at first
    var inital = newsletter.is(":checked");
    var topics = $("#newsletter_topics")[inital ? "removeClass" : "addClass"]("gray");
    var topicInputs = topics.find("input").attr("disabled", !inital);
    // show when newsletter is checked
    newsletter.click(function() {
      topics[this.checked ? "removeClass" : "addClass"]("gray");
      topicInputs.attr("disabled", !this.checked);
    });
  });