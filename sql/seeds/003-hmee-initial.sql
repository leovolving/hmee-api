BEGIN;

INSERT INTO mickeys (park_id, land_id, attraction_id, photo_url, description, hint) VALUES
(2, 5, 15, 'https://i.imgur.com/L17zrC9.jpg', 'queue, x floor', 'Just before you BREAKOUT, look up!'),
(1, 8, 33, 'https://i.imgur.com/fohYsRA.jpg', 'queue near ride entrance', 'Don''t forget your supplies!'),
(1, 15, 74, 'https://i.imgur.com/3EiF76q.jpg', 'queue, x-ray image of a suitcase where a droid is doing security checks', 'This Mickey won''t make it past security!'),
(2, 5, 17, 'https://i.imgur.com/2QIUaTh.jpg', 'queue, TV projection near boarding area', 'This just in: Another Hidden Mickey!'),
(2, 2, null, 'https://i.imgur.com/QsTgY9M.jpg', 'Storefront on an old radio', 'Tune in for this Hidden Mickey!');

COMMIT;