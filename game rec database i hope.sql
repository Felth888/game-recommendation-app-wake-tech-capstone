--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

-- Started on 2023-02-09 13:40:42

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 227 (class 1259 OID 16439)
-- Name: GAMES; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."GAMES" (
    id bigint NOT NULL,
    title character varying(64) NOT NULL,
    developer character varying(32),
    review_score double precision,
    rating character varying(4),
    year_released date
);


ALTER TABLE public."GAMES" OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16438)
-- Name: GAMES_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAMES_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAMES_id_seq" OWNER TO postgres;

--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 226
-- Name: GAMES_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAMES_id_seq" OWNED BY public."GAMES".id;


--
-- TOC entry 242 (class 1259 OID 16499)
-- Name: GAMES2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."GAMES2" (
    id bigint DEFAULT nextval('public."GAMES_id_seq"'::regclass) NOT NULL,
    title character varying(64) NOT NULL,
    developer character varying(32),
    review_score double precision,
    rating character varying(4),
    year_released date
);


ALTER TABLE public."GAMES2" OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 16470)
-- Name: GAME_GENRES; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."GAME_GENRES" (
    id bigint NOT NULL,
    genre_id bigint NOT NULL,
    game_id bigint NOT NULL
);


ALTER TABLE public."GAME_GENRES" OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 16489)
-- Name: GAME_GENRES_game_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAME_GENRES_game_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAME_GENRES_game_id_seq" OWNER TO postgres;

--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 241
-- Name: GAME_GENRES_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAME_GENRES_game_id_seq" OWNED BY public."GAME_GENRES".game_id;


--
-- TOC entry 240 (class 1259 OID 16483)
-- Name: GAME_GENRES_genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAME_GENRES_genre_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAME_GENRES_genre_id_seq" OWNER TO postgres;

--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 240
-- Name: GAME_GENRES_genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAME_GENRES_genre_id_seq" OWNED BY public."GAME_GENRES".genre_id;


--
-- TOC entry 236 (class 1259 OID 16469)
-- Name: GAME_GENRES_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAME_GENRES_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAME_GENRES_id_seq" OWNER TO postgres;

--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 236
-- Name: GAME_GENRES_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAME_GENRES_id_seq" OWNED BY public."GAME_GENRES".id;


--
-- TOC entry 231 (class 1259 OID 16450)
-- Name: GAME_PLATFORMS; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."GAME_PLATFORMS" (
    game_id bigint NOT NULL,
    platform_id bigint NOT NULL,
    id bigint NOT NULL
);


ALTER TABLE public."GAME_PLATFORMS" OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16447)
-- Name: GAME_PLATFORMS_game_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAME_PLATFORMS_game_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAME_PLATFORMS_game_id_seq" OWNER TO postgres;

--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 228
-- Name: GAME_PLATFORMS_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAME_PLATFORMS_game_id_seq" OWNED BY public."GAME_PLATFORMS".game_id;


--
-- TOC entry 230 (class 1259 OID 16449)
-- Name: GAME_PLATFORMS_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAME_PLATFORMS_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAME_PLATFORMS_id_seq" OWNER TO postgres;

--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 230
-- Name: GAME_PLATFORMS_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAME_PLATFORMS_id_seq" OWNED BY public."GAME_PLATFORMS".id;


--
-- TOC entry 229 (class 1259 OID 16448)
-- Name: GAME_PLATFORMS_platform_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GAME_PLATFORMS_platform_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GAME_PLATFORMS_platform_id_seq" OWNER TO postgres;

--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 229
-- Name: GAME_PLATFORMS_platform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GAME_PLATFORMS_platform_id_seq" OWNED BY public."GAME_PLATFORMS".platform_id;


--
-- TOC entry 239 (class 1259 OID 16477)
-- Name: GENRES; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."GENRES" (
    id bigint NOT NULL,
    genre character varying(32) NOT NULL
);


ALTER TABLE public."GENRES" OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 16476)
-- Name: GENRES_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."GENRES_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."GENRES_id_seq" OWNER TO postgres;

--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 238
-- Name: GENRES_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."GENRES_id_seq" OWNED BY public."GENRES".id;


--
-- TOC entry 221 (class 1259 OID 16421)
-- Name: PLATFORMS; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PLATFORMS" (
    id bigint NOT NULL,
    platform character varying(32) NOT NULL
);


ALTER TABLE public."PLATFORMS" OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16420)
-- Name: PLATFORMS_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PLATFORMS_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."PLATFORMS_id_seq" OWNER TO postgres;

--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 220
-- Name: PLATFORMS_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."PLATFORMS_id_seq" OWNED BY public."PLATFORMS".id;


--
-- TOC entry 215 (class 1259 OID 16400)
-- Name: USERS; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."USERS" (
    id bigint NOT NULL,
    user_name character varying(32) NOT NULL,
    email character varying(64) NOT NULL,
    birthdate date NOT NULL,
    password character varying(500) NOT NULL
);


ALTER TABLE public."USERS" OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16430)
-- Name: USER_GAMES; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."USER_GAMES" (
    user_id bigint NOT NULL,
    game_id bigint NOT NULL,
    id bigint NOT NULL
);


ALTER TABLE public."USER_GAMES" OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16428)
-- Name: USER_GAMES_game_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_GAMES_game_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_GAMES_game_id_seq" OWNER TO postgres;

--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 223
-- Name: USER_GAMES_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_GAMES_game_id_seq" OWNED BY public."USER_GAMES".game_id;


--
-- TOC entry 224 (class 1259 OID 16429)
-- Name: USER_GAMES_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_GAMES_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_GAMES_id_seq" OWNER TO postgres;

--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 224
-- Name: USER_GAMES_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_GAMES_id_seq" OWNED BY public."USER_GAMES".id;


--
-- TOC entry 222 (class 1259 OID 16427)
-- Name: USER_GAMES_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_GAMES_user_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_GAMES_user_id_seq" OWNER TO postgres;

--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 222
-- Name: USER_GAMES_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_GAMES_user_id_seq" OWNED BY public."USER_GAMES".user_id;


--
-- TOC entry 235 (class 1259 OID 16461)
-- Name: USER_GENRES; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."USER_GENRES" (
    user_id bigint NOT NULL,
    genre_id bigint NOT NULL,
    id bigint NOT NULL
);


ALTER TABLE public."USER_GENRES" OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 16459)
-- Name: USER_GENRES_genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_GENRES_genre_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_GENRES_genre_id_seq" OWNER TO postgres;

--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 233
-- Name: USER_GENRES_genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_GENRES_genre_id_seq" OWNED BY public."USER_GENRES".genre_id;


--
-- TOC entry 234 (class 1259 OID 16460)
-- Name: USER_GENRES_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_GENRES_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_GENRES_id_seq" OWNER TO postgres;

--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 234
-- Name: USER_GENRES_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_GENRES_id_seq" OWNED BY public."USER_GENRES".id;


--
-- TOC entry 232 (class 1259 OID 16458)
-- Name: USER_GENRES_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_GENRES_user_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_GENRES_user_id_seq" OWNER TO postgres;

--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 232
-- Name: USER_GENRES_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_GENRES_user_id_seq" OWNED BY public."USER_GENRES".user_id;


--
-- TOC entry 218 (class 1259 OID 16408)
-- Name: USER_PLATFORMS; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."USER_PLATFORMS" (
    user_id bigint NOT NULL,
    platform_id bigint NOT NULL,
    id bigint NOT NULL
);


ALTER TABLE public."USER_PLATFORMS" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16406)
-- Name: USER_PLATFORMS_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_PLATFORMS_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_PLATFORMS_id_seq" OWNER TO postgres;

--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 216
-- Name: USER_PLATFORMS_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_PLATFORMS_id_seq" OWNED BY public."USER_PLATFORMS".user_id;


--
-- TOC entry 219 (class 1259 OID 16413)
-- Name: USER_PLATFORMS_id_seq1; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_PLATFORMS_id_seq1"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_PLATFORMS_id_seq1" OWNER TO postgres;

--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 219
-- Name: USER_PLATFORMS_id_seq1; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_PLATFORMS_id_seq1" OWNED BY public."USER_PLATFORMS".id;


--
-- TOC entry 217 (class 1259 OID 16407)
-- Name: USER_PLATFORMS_platform_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."USER_PLATFORMS_platform_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."USER_PLATFORMS_platform_id_seq" OWNER TO postgres;

--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 217
-- Name: USER_PLATFORMS_platform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."USER_PLATFORMS_platform_id_seq" OWNED BY public."USER_PLATFORMS".platform_id;


--
-- TOC entry 214 (class 1259 OID 16399)
-- Name: Users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Users_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Users_id_seq" OWNER TO postgres;

--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 214
-- Name: Users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Users_id_seq" OWNED BY public."USERS".id;


--
-- TOC entry 3235 (class 2604 OID 16442)
-- Name: GAMES id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAMES" ALTER COLUMN id SET DEFAULT nextval('public."GAMES_id_seq"'::regclass);


--
-- TOC entry 3242 (class 2604 OID 16473)
-- Name: GAME_GENRES id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_GENRES" ALTER COLUMN id SET DEFAULT nextval('public."GAME_GENRES_id_seq"'::regclass);


--
-- TOC entry 3243 (class 2604 OID 16484)
-- Name: GAME_GENRES genre_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_GENRES" ALTER COLUMN genre_id SET DEFAULT nextval('public."GAME_GENRES_genre_id_seq"'::regclass);


--
-- TOC entry 3244 (class 2604 OID 16490)
-- Name: GAME_GENRES game_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_GENRES" ALTER COLUMN game_id SET DEFAULT nextval('public."GAME_GENRES_game_id_seq"'::regclass);


--
-- TOC entry 3236 (class 2604 OID 16453)
-- Name: GAME_PLATFORMS game_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_PLATFORMS" ALTER COLUMN game_id SET DEFAULT nextval('public."GAME_PLATFORMS_game_id_seq"'::regclass);


--
-- TOC entry 3237 (class 2604 OID 16454)
-- Name: GAME_PLATFORMS platform_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_PLATFORMS" ALTER COLUMN platform_id SET DEFAULT nextval('public."GAME_PLATFORMS_platform_id_seq"'::regclass);


--
-- TOC entry 3238 (class 2604 OID 16455)
-- Name: GAME_PLATFORMS id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_PLATFORMS" ALTER COLUMN id SET DEFAULT nextval('public."GAME_PLATFORMS_id_seq"'::regclass);


--
-- TOC entry 3245 (class 2604 OID 16480)
-- Name: GENRES id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GENRES" ALTER COLUMN id SET DEFAULT nextval('public."GENRES_id_seq"'::regclass);


--
-- TOC entry 3231 (class 2604 OID 16424)
-- Name: PLATFORMS id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PLATFORMS" ALTER COLUMN id SET DEFAULT nextval('public."PLATFORMS_id_seq"'::regclass);


--
-- TOC entry 3227 (class 2604 OID 16403)
-- Name: USERS id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USERS" ALTER COLUMN id SET DEFAULT nextval('public."Users_id_seq"'::regclass);


--
-- TOC entry 3232 (class 2604 OID 16433)
-- Name: USER_GAMES user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GAMES" ALTER COLUMN user_id SET DEFAULT nextval('public."USER_GAMES_user_id_seq"'::regclass);


--
-- TOC entry 3233 (class 2604 OID 16434)
-- Name: USER_GAMES game_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GAMES" ALTER COLUMN game_id SET DEFAULT nextval('public."USER_GAMES_game_id_seq"'::regclass);


--
-- TOC entry 3234 (class 2604 OID 16435)
-- Name: USER_GAMES id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GAMES" ALTER COLUMN id SET DEFAULT nextval('public."USER_GAMES_id_seq"'::regclass);


--
-- TOC entry 3239 (class 2604 OID 16464)
-- Name: USER_GENRES user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GENRES" ALTER COLUMN user_id SET DEFAULT nextval('public."USER_GENRES_user_id_seq"'::regclass);


--
-- TOC entry 3240 (class 2604 OID 16465)
-- Name: USER_GENRES genre_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GENRES" ALTER COLUMN genre_id SET DEFAULT nextval('public."USER_GENRES_genre_id_seq"'::regclass);


--
-- TOC entry 3241 (class 2604 OID 16466)
-- Name: USER_GENRES id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GENRES" ALTER COLUMN id SET DEFAULT nextval('public."USER_GENRES_id_seq"'::regclass);


--
-- TOC entry 3228 (class 2604 OID 16411)
-- Name: USER_PLATFORMS user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_PLATFORMS" ALTER COLUMN user_id SET DEFAULT nextval('public."USER_PLATFORMS_id_seq"'::regclass);


--
-- TOC entry 3229 (class 2604 OID 16412)
-- Name: USER_PLATFORMS platform_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_PLATFORMS" ALTER COLUMN platform_id SET DEFAULT nextval('public."USER_PLATFORMS_platform_id_seq"'::regclass);


--
-- TOC entry 3230 (class 2604 OID 16414)
-- Name: USER_PLATFORMS id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_PLATFORMS" ALTER COLUMN id SET DEFAULT nextval('public."USER_PLATFORMS_id_seq1"'::regclass);


--
-- TOC entry 3422 (class 0 OID 16439)
-- Dependencies: 227
-- Data for Name: GAMES; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."GAMES" VALUES (1, 'TEST GAME', 'TEST DEV', 85.5, 'E', NULL);


--
-- TOC entry 3437 (class 0 OID 16499)
-- Dependencies: 242
-- Data for Name: GAMES2; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3432 (class 0 OID 16470)
-- Dependencies: 237
-- Data for Name: GAME_GENRES; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3426 (class 0 OID 16450)
-- Dependencies: 231
-- Data for Name: GAME_PLATFORMS; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3434 (class 0 OID 16477)
-- Dependencies: 239
-- Data for Name: GENRES; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."GENRES" VALUES (1, 'TEST GENRE');


--
-- TOC entry 3416 (class 0 OID 16421)
-- Dependencies: 221
-- Data for Name: PLATFORMS; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."PLATFORMS" VALUES (1, 'PC98');


--
-- TOC entry 3410 (class 0 OID 16400)
-- Dependencies: 215
-- Data for Name: USERS; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."USERS" VALUES (0, 'TESTUSER', 'TEST', '1900-01-01', 'TEST');
INSERT INTO public."USERS" VALUES (1, 'My_Test', 'lcwebb1@my.waketech.edu', '2010-01-01', 'P@SSWORD');


--
-- TOC entry 3420 (class 0 OID 16430)
-- Dependencies: 225
-- Data for Name: USER_GAMES; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3430 (class 0 OID 16461)
-- Dependencies: 235
-- Data for Name: USER_GENRES; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3413 (class 0 OID 16408)
-- Dependencies: 218
-- Data for Name: USER_PLATFORMS; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 226
-- Name: GAMES_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAMES_id_seq"', 1, true);


--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 241
-- Name: GAME_GENRES_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAME_GENRES_game_id_seq"', 1, false);


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 240
-- Name: GAME_GENRES_genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAME_GENRES_genre_id_seq"', 1, false);


--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 236
-- Name: GAME_GENRES_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAME_GENRES_id_seq"', 1, false);


--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 228
-- Name: GAME_PLATFORMS_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAME_PLATFORMS_game_id_seq"', 1, false);


--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 230
-- Name: GAME_PLATFORMS_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAME_PLATFORMS_id_seq"', 1, false);


--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 229
-- Name: GAME_PLATFORMS_platform_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GAME_PLATFORMS_platform_id_seq"', 1, false);


--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 238
-- Name: GENRES_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."GENRES_id_seq"', 1, true);


--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 220
-- Name: PLATFORMS_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PLATFORMS_id_seq"', 1, true);


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 223
-- Name: USER_GAMES_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_GAMES_game_id_seq"', 1, false);


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 224
-- Name: USER_GAMES_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_GAMES_id_seq"', 1, false);


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 222
-- Name: USER_GAMES_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_GAMES_user_id_seq"', 1, false);


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 233
-- Name: USER_GENRES_genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_GENRES_genre_id_seq"', 1, false);


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 234
-- Name: USER_GENRES_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_GENRES_id_seq"', 1, false);


--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 232
-- Name: USER_GENRES_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_GENRES_user_id_seq"', 1, false);


--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 216
-- Name: USER_PLATFORMS_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_PLATFORMS_id_seq"', 1, false);


--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 219
-- Name: USER_PLATFORMS_id_seq1; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_PLATFORMS_id_seq1"', 1, false);


--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 217
-- Name: USER_PLATFORMS_platform_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."USER_PLATFORMS_platform_id_seq"', 1, false);


--
-- TOC entry 3480 (class 0 OID 0)
-- Dependencies: 214
-- Name: Users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Users_id_seq"', 1, true);


--
-- TOC entry 3266 (class 2606 OID 16504)
-- Name: GAMES2 GAMES2_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAMES2"
    ADD CONSTRAINT "GAMES2_pkey" PRIMARY KEY (id);


--
-- TOC entry 3256 (class 2606 OID 16446)
-- Name: GAMES GAMES_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAMES"
    ADD CONSTRAINT "GAMES_pkey" PRIMARY KEY (id);


--
-- TOC entry 3262 (class 2606 OID 16475)
-- Name: GAME_GENRES GAME_GENRES_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_GENRES"
    ADD CONSTRAINT "GAME_GENRES_pkey" PRIMARY KEY (id);


--
-- TOC entry 3258 (class 2606 OID 16457)
-- Name: GAME_PLATFORMS GAME_PLATFORMS_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GAME_PLATFORMS"
    ADD CONSTRAINT "GAME_PLATFORMS_pkey" PRIMARY KEY (id);


--
-- TOC entry 3264 (class 2606 OID 16482)
-- Name: GENRES GENRES_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."GENRES"
    ADD CONSTRAINT "GENRES_pkey" PRIMARY KEY (id);


--
-- TOC entry 3252 (class 2606 OID 16426)
-- Name: PLATFORMS PLATFORMS_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PLATFORMS"
    ADD CONSTRAINT "PLATFORMS_pkey" PRIMARY KEY (id);


--
-- TOC entry 3254 (class 2606 OID 16437)
-- Name: USER_GAMES USER_GAMES_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GAMES"
    ADD CONSTRAINT "USER_GAMES_pkey" PRIMARY KEY (id);


--
-- TOC entry 3260 (class 2606 OID 16468)
-- Name: USER_GENRES USER_GENRES_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_GENRES"
    ADD CONSTRAINT "USER_GENRES_pkey" PRIMARY KEY (id);


--
-- TOC entry 3250 (class 2606 OID 16419)
-- Name: USER_PLATFORMS USER_PLATFORMS_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USER_PLATFORMS"
    ADD CONSTRAINT "USER_PLATFORMS_pkey" PRIMARY KEY (id);


--
-- TOC entry 3248 (class 2606 OID 16405)
-- Name: USERS Users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."USERS"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (id);


-- Completed on 2023-02-09 13:40:42

--
-- PostgreSQL database dump complete
--

