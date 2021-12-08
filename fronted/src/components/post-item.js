
const PostItemm = (props) => {
    const { id, username, email } = props
    return (
        <div>
            <h3>
                {id} - {username} - {email}
            </h3>
        </div>

    );
}

export default PostItemm;