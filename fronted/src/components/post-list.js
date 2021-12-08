import PostItemm from "./post-item"
import { memo } from 'react'

const PostList = (props) => {
    console.log('post list', props.data)
    const { data } = props
    return (
        <div>
            {data.map((item) => {
                return <PostItemm key={item.id} id={item.id} username={item.username} email={item.email} />;
            })}
        </div>
    )
}

export default memo(PostList);