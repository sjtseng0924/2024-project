import api from './api';

export const loginUser = async (userName) => {
  try {
    const response = await api.post(`/newuser/${userName}/`);
    return response.data; // Contains "status" and "uuid"
  } catch (error) {
    if (error.response && error.response.status === 400) {
      // User already exists
      return { status: 'User already exists', uuid: null };
    }
    throw error;
  }
};

export const createChatRoom = async (roomName) => {
  const response = await api.post(`/create/${roomName}/`);
  return response.data;
};

export const registerUser = async (userName) => {
  const response = await api.post(`/newuser/${userName}/`);
  return response.data;
};

export const sendMessage = async (roomName, senderName, messageContent) => {
  const response = await api.post(`/send/${roomName}/`, {
    name: senderName,
    message: messageContent,
  });
  return response.data;
};

export const getAllMessages = async (roomName) => {
  const response = await api.get(`/messages/${roomName}/`);
  return response.data.messages;
};
