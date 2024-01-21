import React, { useState, useEffect, useContext } from "react";
import { useParams, useHistory } from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import MainContext from "../../context/MainContext";
import CommentContainer from "../commentContainer/CommentContainer";
import EditAdPopup from "../editAdPopup/EditAdPopup";
import Buttons from "../buttons/Buttons";
import Preloader from "../preloader/Preloader";
import EditPhotoAdPopup from "../editPhotoPopup/EditPhotoPopup";

function SinglePage() {
  const { id } = useParams();
  const [ad, setAd] = useState({});
  const [comments, setComments] = useState([]);
  const [userInfo, setUserInfo] = useState({});
  let ad_pk = id;
  let { user } = useContext(AuthContext);
  const {
    isEditPopupOpen,
    isEditPhotoPopupOpen,
    closePopup,
    setAds,
    handleOpenEditPopup,
    handleOpenEditPhotoPopup,
    getAd,
    getComments,
    setIsLoading,
    isLoading,
    deleteAdd,
    addComment,
    editAdd,
    editAddPhoto,
    getUserInfo,
  } = useContext(MainContext);
  let history = useHistory();

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (user) {
          setIsLoading(true);

          // Получение информации о пользователе
          const userInfoResponse = await getUserInfo();
          setUserInfo(userInfoResponse.data);

          // Получение комментариев и данных объявления параллельно
          const [commentsData, adData] = await Promise.all([
            getComments(ad_pk),
            getAd(id),
          ]);

          setComments(commentsData.data.results);
          setAd(adData.data);
        }
      } catch (error) {
        console.log("Ошибка при получении данных", error);
      } finally {
        setTimeout(() => setIsLoading(false), 700);
      }
    };

  fetchData();
  // eslint-disable-next-line react-hooks/exhaustive-deps
}, [user]);

  function handleEditAdd(data) {
    debugger;
    editAdd(id, data)
      .then((data) => {
        setAds((ads) => ads.filter((i) => (i.id === ad.id ? data : null)));
        window.location.reload();
      })
      .catch((error) => console.log("error", error));
  }

  function handleEditPhotoAdd(image) {
    editAddPhoto(id, image)
      .then((image) => {
        setAds((ads) => ads.filter((i) => (i.id === ad.id ? image : null)));
        window.location.reload();
      })
      .catch((error) => console.log("error", error));
  }

  function handleDeleteAdd(e) {
    e.preventDefault();
    deleteAdd(id)
      .then(() => {
        setAds((ads) => ads.filter((i) => i.id !== ad.id));
        history.push("/");
      })
      .catch((error) => console.log("error", error));
  }
  function handleAddComment(data) {
    addComment(id, data)
      .then((newComment) => {
        setComments([newComment, ...comments]);
        window.location.reload();
      })
      .catch((error) => console.log("error", error));
  }

  return (
    <main className="cardInformation">
      {isLoading ? (
        <Preloader />
      ) : (
        ad && (
          <>
            <h1 className="cardInformation__title">{ad.title}</h1>
            <div className="cardInformation__container">
              {ad.image === null ? (
                <div className="cardInformation__img-null">
                  {(ad.author && user.user_id === ad.author.id) || userInfo.role === 'admin' ? (
                    <button
                      onClick={() => handleOpenEditPhotoPopup()}
                      className="cardInformation__img-change"
                      type="button"
                    />
                  ) : null}
                </div>
              ) : (
                <div
                  style={{ backgroundImage: `url(${ad.image})` }}
                  className="cardInformation__img"
                >
                  {(ad.author && user.user_id === ad.author.id) || userInfo.role === 'admin' ? (
                    <button
                      onClick={() => handleOpenEditPhotoPopup()}
                      className="cardInformation__img-change"
                      type="button"
                    />
                  ) : null}
                </div>
              )}
              {(ad.author && user.user_id === ad.author.id) || userInfo.role === 'admin' ? (
                <Buttons
                  user={user}
                  product={ad}
                  onOpen={handleOpenEditPopup}
                  className="buttons"
                  classButton="buttons-item"
                  onSubmit={handleDeleteAdd}
                />
              ): null}
              <div className="cardInformation__box">
                <p className="cardInformation__price">Цена: {ad.price} &#8381;</p>
              </div>
              <div className="cardInformation__box">
                <p className="cardInformation__description">{ad.description}</p>
              </div>
              <div className="cardInformation__box">
                {ad.author && ad.author.phone && ad.author.first_name ? (
                  <div className="cardInformation__box_second">
                    <p className="cardInformation__tel">{ad.author.phone}</p>
                    <p className="cardInformation__tel">{ad.author.first_name}</p>
                  </div>
                ) : null}
              </div>
              <CommentContainer
                comments={comments}
                addComment={handleAddComment}
                setComments={setComments}
                user={user}
              />
            </div>
            <EditAdPopup
              isEditPopupOpen={isEditPopupOpen}
              onClose={closePopup}
              handleEditAdd={handleEditAdd}
              id={id}
              ad={ad}
            />
            <EditPhotoAdPopup
              id={id}
              handleEdit={handleEditPhotoAdd}
              isOpen={isEditPhotoPopupOpen}
              onClose={closePopup}
            />
          </>
        )
      )}
    </main>
  );
}

export default SinglePage;
