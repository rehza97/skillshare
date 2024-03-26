function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");


let form = document.getElementById("send-message-form");
const receiverId = "{{ receiver.id }}"; // Get the receiver ID from the template
console.log(receiverId)
const url = `/sent/${receiverId}/`;
form.addEventListener("submit", sendChat);
async function sendChat(e) {
  e.preventDefault();
  let ChatMsg = document.getElementById("input-message").value; // Get the message content
  const data = { msg: ChatMsg };
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    console.log("Success:", result);
    console.log(response);
    // let chatMsgElement = createChatMessageElement(result["sender"], result['message']);
    document.getElementById("id_body").value = ""; // Clear the message input field after sending
  } catch (error) {
    console.error("Error:", error);
  }
}
