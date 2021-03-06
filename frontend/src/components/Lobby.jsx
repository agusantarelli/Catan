import React, { useEffect, useState } from "react";
import { Redirect, useParams, useHistory } from "react-router-dom";

import { ReactComponent as Crown } from "../public/icons/crown-solid.svg";
import { ReactComponent as Dot } from "../public/icons/circle-solid.svg";
import { ReactComponent as AlertIcon } from "../public/icons/exclamation-triangle-solid.svg";
import { ReactComponent as NormalUser } from "../public/icons/user-shield-solid.svg";

import api from "../Api";

const TextClasses = "text-center text-sm tracking-wider text-bold text-white";
const CommonClasses =
  "h-12 shadow-md shadow rounded cursor-pointer disabled:cursor-not-allowed disabled:opacity-50";
// TODO: Change all names with Lobby to Room, they are the same
function Lobby() {
  const { roomId } = useParams();
  const history = useHistory();
  const [room, setRoom] = useState();

  useEffect(() => {
    const fetchRoom = async () => {
      const res = await api.lobbies.get(roomId);
      setRoom(res.data);
    };
    fetchRoom();
    const interval = setInterval(() => fetchRoom(), api.POLL_EVERY);
    return () => clearInterval(interval);
  }, [roomId]);

  const handleJoin = async event => {
    event.preventDefault();
    try {
      const res = await api.lobbies.join(roomId);
      console.log(res); // TODO: Handle join response
    } catch (err) {
      console.log(`Error: ${err}`);
    }
  };

  const handleStartGame = async event => {
    event.preventDefault();
    try {
      const res = await api.lobbies.start(roomId);
      console.log(res); // TODO: Handle start response
    } catch (err) {
      console.log(`Error: ${err}`);
    }
  };

  const handleCancelGame = async event => {
    event.preventDefault();
    if (!window.confirm("You're about to cancel the lobby. Confirm?")) return;
    try {
      history.push(`/lobby`);
      const res = await api.lobbies.cancel(roomId);
      console.log(res); // TODO: Handle start response
    } catch (err) {
      console.log(`Error: ${err}`);
    }
  };

  if (!room) return <div> Loading! </div>;
  return (
    <div className="h-full bg-orange-300">
      <div className="py-5 flex flex-col">
        <h1 className="font-cinzel text-gray-900 text-5xl lg:text-6xl lg:text-bold md:pt-5 lg:pt-5 self-center">
          {room.name}
        </h1>
        <div className="w-11/12 md:w-8/12 self-center">
          <ul className="w-full rounded-lg mt-4 shadow-md">
            {room.players.map((player, index) => (
              <li
                key={player}
                className={`
                  py-4 px-6
                  w-full
                  text-gray-900 truncate
                  ${index === 0 ? "rounded-t-lg" : ""}
                  ${index % 2 ? "bg-gray-200" : "bg-gray-300"}
                  ${index === room.players.length - 1 ? "rounded-b-lg" : ""}
                `}
              >
                <div className="flex flex-row justify-between items-center">
                  <div className="flex flex-row">
                    <div
                      className={`w-6 h-6 mr-5 ${
                        player === room.owner
                          ? "text-blue-900"
                          : "text-gray-600"
                      }`}
                    >
                      {player === room.owner ? <Crown /> : <NormalUser />}
                    </div>
                    <span>{player}</span>
                  </div>
                  <div className="self-center w-3 h-3 mr-5 text-green-600">
                    <Dot />
                  </div>
                </div>
              </li>
            ))}
          </ul>

          {room.players.length < 3 ? (
            <span className="text-red-700 flex flex-row m-3">
              <div className="w-6 h-6 mr-4">
                <AlertIcon />
              </div>
              ??Necesitas {3 - room.players.length} m??s en la partida!
            </span>
          ) : (
            <div className="m-4" />
          )}
          <input
            type="button"
            value="JOIN GAME"
            disabled={
              !(room.players.length < room.max_players) ||
              room.game_has_started ||
              room.players.includes(localStorage.user)
              // TODO: this should not get the user from localStorage
            }
            onClick={handleJoin}
            className={`
              w-full
              bg-orange-600
              ${CommonClasses}
              ${TextClasses}
            `}
          />
          <div className="m-4" />
          {!room.game_has_started && room.owner === localStorage.user && (
            <div className="flex items-center justify-between">
              <input
                type="button"
                value="CANCEL GAME"
                onClick={handleCancelGame}
                className={`
                  w-1/2
                  bg-red-800
                  ${CommonClasses}
                  ${TextClasses}
                `}
              />
              <div className="m-2" />
              <input
                type="button"
                value="START GAME"
                disabled={
                  !(
                    room.players.length >= 3 &&
                    room.players.length <= room.max_players
                  )
                }
                onClick={handleStartGame}
                className={`
                  w-1/2
                  bg-green-800
                  ${CommonClasses}
                  ${TextClasses}
                `} // TODO: Green? Rly?
              />
            </div>
          )}
          {room.game_has_started && <Redirect to={`/game/${room.game_id}`} />}
        </div>
      </div>
    </div>
  );
}

export default Lobby;
