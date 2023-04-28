import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  const result = { photo: null, user: null };
  let userResults = null;
  let photoResults = null;

  try {
    userResults = await createUser();
  } catch (e) {
    console.log(e);
  }

  try {
    photoResults = await uploadPhoto();
  } catch (e) {
    console.log(e);
  }

  return result;
}

