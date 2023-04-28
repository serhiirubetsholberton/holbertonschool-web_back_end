import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const result = [];
  return signUpUser(firstName, lastName)
    .then((userResult) => {
      result.push({
        status: 'fulfilled',
        value: userResult,
      });

      return uploadPhoto(fileName)
        .then((photoResult) => {
          result.push({
            status: 'fulfilled',
            value: photoResult,
          });
          return result;
        })
        .catch((photoError) => {
          result.push({
            status: 'rejected',
            value: photoError.toString(),
          });
          return result;
        });
    });
}
