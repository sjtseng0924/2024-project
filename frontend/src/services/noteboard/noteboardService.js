import api from './api';

export const createNote = async (noteContent) => {
  const response = await api.post(`/add/`, {
    note_content: noteContent,
  });
  return response.data; // Contains "status" and "uuid"
};

export const getAllNotes = async () => {
  const response = await api.get(`/get/`);
  return response.data;
};

export const findNote = async (NoteID) => {
  const response = await api.get(`/get/${NoteID}/`);
  return response.data;
};

export const updateLikes = async (NoteID, likes) => {
  const response = await api.post(`/update_likes/${NoteID}/`, {
    likes: likes 
  });
  return response.data; 
};
