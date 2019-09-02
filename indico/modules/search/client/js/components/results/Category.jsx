import React from 'react';
import {List} from 'semantic-ui-react';
import PropTypes from 'prop-types';
import CategoryPath from './CategoryPath';
import './Category.module.scss';

export default function Category({title, path, url}) {
  return (
    <div styleName="category">
      <List.Header>
        <a href={url}>{title}</a>
      </List.Header>
      <div styleName="description">
        {path.length !== 0 && (
          <List.Description>
            <CategoryPath path={path} />
          </List.Description>
        )}
      </div>
    </div>
  );
}

Category.propTypes = {
  title: PropTypes.string.isRequired,
  path: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      url: PropTypes.string.isRequired,
    })
  ).isRequired,
  url: PropTypes.string.isRequired,
};
