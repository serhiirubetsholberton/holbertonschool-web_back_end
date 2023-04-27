export default function getFullResponseFromAPI(success) {
  if (success) {
    return new Promise((res, rej) => {
      if (success) {
        return res({
          status: 200,
          body: 'Success'
        })
      }

      rej('The fake API is not working currently');
    });
  }
}
