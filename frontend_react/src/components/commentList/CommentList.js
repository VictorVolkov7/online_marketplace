import React from "react";
import Comment from "../comment/Comment";

function CommentList({ comments, setComments, user }) {
  return (
    <>
      {!comments.length ? (
        <p className="comment-text">Оставтье комментарий первым.</p>
      ) : (
        <ul className="comment-list">
          {comments.map((comment) => {
            return (
              <Comment
                key={comment.id}
                text={comment.text}
                adId={comment.ad}
                img={comment.author.image}
                commentId={comment.id}
                userId={comment.author.id}
                setComments={setComments}
                authorName={comment.author.first_name}
                user={user}
              />
            );
          })}
        </ul>
      )}
    </>
  );
}

export default CommentList;
