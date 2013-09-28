--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: domain_id_seq; Type: SEQUENCE; Schema: public; Owner: aelaguiz
--

CREATE SEQUENCE domain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.domain_id_seq OWNER TO aelaguiz;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: domain; Type: TABLE; Schema: public; Owner: aelaguiz; Tablespace: 
--

CREATE TABLE domain (
    id bigint DEFAULT nextval('domain_id_seq'::regclass) NOT NULL,
    domain character varying NOT NULL
);


ALTER TABLE public.domain OWNER TO aelaguiz;

--
-- Name: domain_traffic; Type: TABLE; Schema: public; Owner: aelaguiz; Tablespace: 
--

CREATE TABLE domain_traffic (
    id bigint NOT NULL,
    organic_keywords integer NOT NULL,
    organic_traffic integer NOT NULL,
    organic_cost integer NOT NULL,
    adwords_keywords integer NOT NULL,
    adwords_traffic integer NOT NULL,
    adwords_cost integer NOT NULL,
    rank integer NOT NULL
);


ALTER TABLE public.domain_traffic OWNER TO aelaguiz;

--
-- Name: keyword_id_seq; Type: SEQUENCE; Schema: public; Owner: aelaguiz
--

CREATE SEQUENCE keyword_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.keyword_id_seq OWNER TO aelaguiz;

--
-- Name: keyword; Type: TABLE; Schema: public; Owner: aelaguiz; Tablespace: 
--

CREATE TABLE keyword (
    id bigint DEFAULT nextval('keyword_id_seq'::regclass) NOT NULL,
    keyword character varying NOT NULL
);


ALTER TABLE public.keyword OWNER TO aelaguiz;

--
-- Name: keyword_competition; Type: TABLE; Schema: public; Owner: aelaguiz; Tablespace: 
--

CREATE TABLE keyword_competition (
    id bigint NOT NULL,
    cpc double precision NOT NULL,
    competition double precision NOT NULL,
    search_volume bigint NOT NULL,
    num_results bigint NOT NULL
);


ALTER TABLE public.keyword_competition OWNER TO aelaguiz;

--
-- Name: organic_map; Type: TABLE; Schema: public; Owner: aelaguiz; Tablespace: 
--

CREATE TABLE organic_map (
    "position" integer NOT NULL,
    keyword_id bigint NOT NULL,
    url_id bigint NOT NULL
);


ALTER TABLE public.organic_map OWNER TO aelaguiz;

--
-- Name: organic_rank_id_seq; Type: SEQUENCE; Schema: public; Owner: aelaguiz
--

CREATE SEQUENCE organic_rank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organic_rank_id_seq OWNER TO aelaguiz;

--
-- Name: url_id_seq; Type: SEQUENCE; Schema: public; Owner: aelaguiz
--

CREATE SEQUENCE url_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.url_id_seq OWNER TO aelaguiz;

--
-- Name: url; Type: TABLE; Schema: public; Owner: aelaguiz; Tablespace: 
--

CREATE TABLE url (
    id bigint DEFAULT nextval('url_id_seq'::regclass) NOT NULL,
    url character varying NOT NULL,
    domain_id bigint NOT NULL
);


ALTER TABLE public.url OWNER TO aelaguiz;

--
-- Name: domain_domain_key; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY domain
    ADD CONSTRAINT domain_domain_key UNIQUE (domain);


--
-- Name: domain_pkey; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY domain
    ADD CONSTRAINT domain_pkey PRIMARY KEY (id);


--
-- Name: domain_traffic_pkey; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY domain_traffic
    ADD CONSTRAINT domain_traffic_pkey PRIMARY KEY (id);


--
-- Name: keyword_competition_pkey; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY keyword_competition
    ADD CONSTRAINT keyword_competition_pkey PRIMARY KEY (id);


--
-- Name: keyword_keyword_key; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY keyword
    ADD CONSTRAINT keyword_keyword_key UNIQUE (keyword);


--
-- Name: keyword_pkey; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY keyword
    ADD CONSTRAINT keyword_pkey PRIMARY KEY (id);


--
-- Name: organic_map_pkey; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY organic_map
    ADD CONSTRAINT organic_map_pkey PRIMARY KEY (keyword_id, url_id);


--
-- Name: url_pkey; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY url
    ADD CONSTRAINT url_pkey PRIMARY KEY (id);


--
-- Name: url_url_key; Type: CONSTRAINT; Schema: public; Owner: aelaguiz; Tablespace: 
--

ALTER TABLE ONLY url
    ADD CONSTRAINT url_url_key UNIQUE (url);


--
-- Name: domain_traffic_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aelaguiz
--

ALTER TABLE ONLY domain_traffic
    ADD CONSTRAINT domain_traffic_id_fkey FOREIGN KEY (id) REFERENCES domain(id) ON DELETE CASCADE;


--
-- Name: keyword_competition_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aelaguiz
--

ALTER TABLE ONLY keyword_competition
    ADD CONSTRAINT keyword_competition_id_fkey FOREIGN KEY (id) REFERENCES keyword(id) ON DELETE CASCADE;


--
-- Name: organic_map_keyword_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aelaguiz
--

ALTER TABLE ONLY organic_map
    ADD CONSTRAINT organic_map_keyword_id_fkey FOREIGN KEY (keyword_id) REFERENCES keyword(id) ON DELETE CASCADE;


--
-- Name: organic_map_url_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aelaguiz
--

ALTER TABLE ONLY organic_map
    ADD CONSTRAINT organic_map_url_id_fkey FOREIGN KEY (url_id) REFERENCES url(id) ON DELETE CASCADE;


--
-- Name: url_domain_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aelaguiz
--

ALTER TABLE ONLY url
    ADD CONSTRAINT url_domain_id_fkey FOREIGN KEY (domain_id) REFERENCES domain(id) ON DELETE CASCADE;


--
-- Name: public; Type: ACL; Schema: -; Owner: aelaguiz
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM aelaguiz;
GRANT ALL ON SCHEMA public TO aelaguiz;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

