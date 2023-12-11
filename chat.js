const axios = require('axios');
const { createMessage, getMultipleMessages, createConversation, getSingleConversationById } = require("../../controllers/message");
const { socketTryCatcher } = require("../../utils/controllers");

// ...

const sendToRasa = async (messageContent) => {
  const url = 'http://2859-35-201-167-238.ngrok.io/webhooks/rest/webhook'; // Remplacez par votre URL Rasa
  try {
    const response = await axios.post(url, { message: messageContent });
    return response.data; // Récupérez la réponse du chatbot Rasa
  } catch (error) {
    console.error('Erreur lors de la communication avec le chatbot Rasa :', error);
    return null; // Gérer les erreurs de requête
  }
};

const newMessagesHandler = socketTryCatcher(async (_io, socket, data = {}) => {
  // ... 

  const userMessageContent = newMessage.content; // Obtenez le contenu du message utilisateur
  const aiReply = await sendToRasa(userMessageContent); // Appel à votre chatbot Rasa

  const userId = socket.user._id.toString();
  const aiMessage = await createMessage({
    conversation: conversation._id,
    conversationOwner: userId,
    role: "assistant",
    content: aiReply ? aiReply[0].text : "Sorry, I didn't understand that.",
  });

  socket.emit(events.new, {
    conversation,
    messages: [starterMessage, newUserMessage, aiMessage].filter((it) =>
      Boolean(it)
    ),
  });
});

// ...
