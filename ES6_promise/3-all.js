import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return new Promise((res) => {
    uploadPhoto()
      .then(({ body }) => {
        createUser()
          .then(({ firstName, lastName }) => {
            console.log(`${body} ${firstName} ${lastName}`);
            res();
          });
      });
  })
}
