import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const result = [];
  return signUpUser(firstName, lastName)
    .then((userResult) => {
      result.push({
        status: 'success',
        value: userResult,
      });

      uploadPhoto(fileName)
        .then((photoResult) => {
          result.push({
            status: 'success',
            value: photoResult,
          });
          return result;
        })
        .catch((photoError) => {
          result.push({
            status: 'error',
            value: photoError,
          });
          return result;
        });
    });
}
