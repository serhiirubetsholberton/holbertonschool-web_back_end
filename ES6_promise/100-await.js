import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
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

  return { photo: photoResults, user: userResults };
}
