import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  uploadPhoto()
    .then(({ body }) => {
      console.log(body);
    });

  createUser()
    .then(({ firstName, lastName }) => {
      console.log(firstName, lastName);
    })
}
