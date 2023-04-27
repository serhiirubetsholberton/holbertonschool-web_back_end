import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  uploadPhoto()
    .then(({ body }) => {
      createUser()
        .then(({ firstName, lastName }) => {
          console.log(body, firstName, lastName);
        });
    });
}
